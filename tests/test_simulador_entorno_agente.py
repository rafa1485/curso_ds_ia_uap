import unittest

import numpy as np
import pandas as pd

from MATERIAL_CURSOS.LABORATORIOS.MOVILIDAD import simulador_entorno_agente


class SimuladorEntornoAgenteTestCase(unittest.TestCase):
    def setUp(self):
        self.centros = pd.DataFrame(
            {
                "LocationID": [1, 2],
                "zona": ["Zona objetivo", "Otra zona"],
                "latitud": [40.7, 40.8],
                "longitud": [-74.0, -73.9],
            }
        )

    def test_tasa_esperada_disminuye_con_la_flota_de_x(self):
        tasa_sin_taxis = simulador_entorno_agente.tasa_otras_esperada(0)
        tasa_flota_grande = simulador_entorno_agente.tasa_otras_esperada(100)

        self.assertGreater(tasa_sin_taxis, tasa_flota_grande)
        self.assertGreaterEqual(tasa_flota_grande, simulador_entorno_agente.Q_OTRAS_MIN)
        self.assertLessEqual(tasa_sin_taxis, simulador_entorno_agente.Q_OTRAS_MAX)

    def test_percepcion_conserva_la_demanda_y_respeta_capacidad(self):
        viajes = pd.DataFrame({"PULocationID": [1] * 100 + [2] * 20})

        percepcion = simulador_entorno_agente.construir_percepcion(
            viajes,
            self.centros,
            zona_id=1,
            hora=8,
            taxis_x=20,
            generador=np.random.default_rng(42),
        )

        self.assertEqual(percepcion["demanda_total"], 100)
        self.assertEqual(
            percepcion["demanda_total"],
            percepcion["viajes_otras"] + percepcion["demanda_x"],
        )
        self.assertEqual(percepcion["capacidad_x"], 20)
        self.assertEqual(
            percepcion["viajes_atendibles_x"],
            min(percepcion["demanda_x"], percepcion["capacidad_x"]),
        )
        self.assertGreaterEqual(
            percepcion["tasa_otras_simulada"],
            simulador_entorno_agente.Q_OTRAS_MIN,
        )
        self.assertLessEqual(
            percepcion["tasa_otras_simulada"],
            simulador_entorno_agente.Q_OTRAS_MAX,
        )

    def test_percepcion_es_reproducible(self):
        viajes = pd.DataFrame({"PULocationID": [1] * 50})

        primera = simulador_entorno_agente.construir_percepcion(
            viajes, self.centros, 1, 8, 10, np.random.default_rng(7)
        )
        segunda = simulador_entorno_agente.construir_percepcion(
            viajes, self.centros, 1, 8, 10, np.random.default_rng(7)
        )

        self.assertEqual(primera, segunda)

    def test_separa_h_mas_uno_de_las_percepciones(self):
        escenario = pd.DataFrame(
            {
                "hora": [6, 7, 8],
                "demanda_x": [4, 6, 10],
                "capacidad_x": [8, 8, 8],
                "demanda_no_cubierta_x": [0, 0, 2],
            }
        )

        visible, futuro = simulador_entorno_agente.separar_escenario(
            escenario, hora_decision=7
        )

        self.assertEqual(visible["hora"].tolist(), [6, 7])
        self.assertEqual(futuro["hora"].tolist(), [8])
        self.assertTrue(futuro.loc[0, "necesita_refuerzo"])
        self.assertEqual(futuro.loc[0, "taxis_adicionales_sugeridos"], 2)
        self.assertNotIn("necesita_refuerzo", visible.columns)

    def test_escenario_sintetico_no_filtra_el_futuro(self):
        fechas = []
        pickup = []
        dropoff = []
        for dia in [1, 8, 15, 22, 29]:
            for hora in [7, 8, 9]:
                for minuto in range(20):
                    fechas.append(f"2024-01-{dia:02d} {hora:02d}:{minuto:02d}:00")
                    pickup.append(1)
                    dropoff.append(2)
        viajes = pd.DataFrame(
            {
                "tpep_pickup_datetime": fechas,
                "PULocationID": pickup,
                "DOLocationID": dropoff,
            }
        )

        primero = simulador_entorno_agente.simular_escenario(
            viajes,
            self.centros,
            zona_id=1,
            hora_decision=8,
            taxis_x=10,
            anio=2024,
            mes=1,
            horas_historia=2,
            semilla=123,
        )
        segundo = simulador_entorno_agente.simular_escenario(
            viajes,
            self.centros,
            zona_id=1,
            hora_decision=8,
            taxis_x=10,
            anio=2024,
            mes=1,
            horas_historia=2,
            semilla=123,
        )
        visible, futuro = simulador_entorno_agente.separar_escenario(primero, 8)

        pd.testing.assert_frame_equal(primero, segundo)
        self.assertEqual(visible["hora"].tolist(), [7, 8])
        self.assertEqual(futuro["hora"].tolist(), [9])

    def test_rechaza_historia_anterior_al_lunes(self):
        with self.assertRaisesRegex(ValueError, "horas_historia"):
            simulador_entorno_agente.simular_escenario(
                pd.DataFrame(),
                self.centros,
                zona_id=1,
                hora_decision=1,
                taxis_x=10,
                anio=2024,
                mes=1,
                horas_historia=3,
            )

    def test_rechaza_hora_no_entera(self):
        with self.assertRaisesRegex(TypeError, "hora"):
            simulador_entorno_agente.construir_percepcion(
                pd.DataFrame({"PULocationID": [1]}),
                self.centros,
                zona_id=1,
                hora=8.5,
                taxis_x=10,
                generador=np.random.default_rng(1),
            )


if __name__ == "__main__":
    unittest.main()
