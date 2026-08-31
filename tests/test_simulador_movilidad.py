import importlib.util
import unittest
from pathlib import Path

import numpy as np
import pandas as pd


RUTA_SIMULADOR = (
    Path(__file__).parents[1]
    / "MATERIAL_CURSOS"
    / "LABORATORIOS"
    / "MOVILIDAD"
    / "simulador_movilidad.py"
)
SPEC = importlib.util.spec_from_file_location("simulador_movilidad", RUTA_SIMULADOR)
simulador = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(simulador)


class SimuladorMovilidadTestCase(unittest.TestCase):
    def setUp(self):
        self.centros = pd.DataFrame(
            {
                "LocationID": [1, 2],
                "zona": ["Origen", "Destino"],
                "latitud": [0.0, 0.0],
                "longitud": [0.0, 1.0],
            }
        )

    def test_estima_promedio_sobre_todos_los_lunes_del_mes(self):
        viajes = pd.DataFrame(
            {
                "tpep_pickup_datetime": [
                    "2024-01-01 08:10:00",
                    "2024-01-01 08:20:00",
                    "2024-01-08 08:30:00",
                    "2024-01-09 08:30:00",
                ],
                "PULocationID": [1, 1, 2, 1],
                "DOLocationID": [2, 2, 1, 2],
            }
        )

        tasa, od = simulador.estimar_modelo_demanda(
            viajes, self.centros, hora=8, anio=2024, mes=1
        )

        self.assertEqual(tasa, 3 / 5)
        probabilidades = {
            (fila.PULocationID, fila.DOLocationID): fila.probabilidad
            for fila in od.itertuples()
        }
        self.assertAlmostEqual(probabilidades[(1, 2)], 2 / 3)
        self.assertAlmostEqual(probabilidades[(2, 1)], 1 / 3)

    def test_simulacion_es_reproducible_y_genera_minutos_validos(self):
        od = pd.DataFrame(
            {
                "PULocationID": [1, 2],
                "DOLocationID": [2, 1],
                "probabilidad": [0.75, 0.25],
            }
        )

        primero = simulador.simular_viajes(20, od, self.centros, 8, semilla=42)
        segundo = simulador.simular_viajes(20, od, self.centros, 8, semilla=42)

        pd.testing.assert_frame_equal(primero, segundo)
        self.assertTrue(primero["minuto"].between(0, 59).all())
        self.assertTrue(primero["minuto"].is_monotonic_increasing)
        self.assertTrue((primero["distancia_centros_km"] > 111).all())
        self.assertTrue((primero["distancia_centros_km"] < 112).all())

    def test_haversine_es_cero_para_el_mismo_centro(self):
        distancia = simulador.distancia_haversine_km([40.7], [-74.0], [40.7], [-74.0])
        np.testing.assert_allclose(distancia, [0.0])

    def test_rechaza_hora_invalida(self):
        with self.assertRaisesRegex(ValueError, "hora"):
            simulador.estimar_modelo_demanda(
                pd.DataFrame(), self.centros, hora=24, anio=2024, mes=1
            )


if __name__ == "__main__":
    unittest.main()
