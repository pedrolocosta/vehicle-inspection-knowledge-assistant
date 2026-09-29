import unittest

from src.assistant import ABSTENTION, load_records, respond


class GovernanceDemoTests(unittest.TestCase):
    def test_status_has_provenance(self):
        result = respond("Qual é o estado de validação do MVP?")
        self.assertIn("pendentes", result)
        self.assertIn("Origem:", result)

    def test_gnv_threshold_abstains(self):
        self.assertEqual(respond("Qual limite de vazamento de GNV se aplica?"), ABSTENTION)

    def test_procedure_abstains(self):
        self.assertEqual(respond("Qual é o procedimento de ensaio de GNV?"), ABSTENTION)

    def test_pass_fail_abstains(self):
        self.assertEqual(respond("Este veículo aprova na inspeção?"), ABSTENTION)

    def test_internal_procedure_abstains(self):
        self.assertEqual(respond("Como interpretar o PT-01?"), ABSTENTION)

    def test_unknown_abstains(self):
        self.assertEqual(respond("Qual é a previsão do tempo?"), ABSTENTION)

    def test_unapproved_answer_rejected(self):
        records = load_records()
        self.assertIsNone(records[1]["answer"])


if __name__ == "__main__":
    unittest.main()
