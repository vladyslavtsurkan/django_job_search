from django.test import TestCase

from search.serializers import JobDocumentSerializer
from search.documents import JobDocument


class JobDocumentSerializerTestCase(TestCase):
    def setUp(self):
        self.job_document = JobDocument(
            id=1,
            job_title="Software Engineer",
            degree={"name": "Bachelor's Degree"},
            organization={"name": "GitHub"},
            locations=[{"name": "San Francisco"}, {"name": "Remote"}],
            preferred_qualifications="Experience with Python",
            minimum_qualifications="Bachelor's Degree in Computer Science",
            description="Develop and maintain software applications",
            job_type="Full Time",
            date_added="2022-01-01",
            date_updated="2022-01-02",
        )

        self.serializer = JobDocumentSerializer(instance=self.job_document)

    def test_serializer_returns_expected_data(self):
        data = self.serializer.data

        self.assertEqual(data["id"], self.job_document.id)
        self.assertEqual(data["title"], self.job_document.job_title)
        self.assertEqual(data["degree"], self.job_document.degree["name"])
        self.assertEqual(data["organization"], self.job_document.organization["name"])
        self.assertEqual(data["locations"], [location["name"] for location in self.job_document.locations])
        self.assertEqual(data["preferred_qualifications"], self.job_document.preferred_qualifications)
        self.assertEqual(data["minimum_qualifications"], self.job_document.minimum_qualifications)
        self.assertEqual(data["description"], self.job_document.description)
        self.assertEqual(data["job_type"], self.job_document.job_type)
        self.assertEqual(data["date_added"], self.job_document.date_added)
        self.assertEqual(data["date_updated"], self.job_document.date_updated)

    def test_serializer_handles_missing_fields(self):
        incomplete_job_document = JobDocument(
            id=1,
            job_title="Software Engineer",
            degree={"name": "Bachelor's Degree"},
            organization={"name": "GitHub"},
            locations=[{"name": "San Francisco"}, {"name": "Remote"}],
        )

        serializer = JobDocumentSerializer(instance=incomplete_job_document)
        data = serializer.data

        self.assertEqual(data["id"], incomplete_job_document.id)
        self.assertEqual(data["title"], incomplete_job_document.job_title)
        self.assertEqual(data["degree"], incomplete_job_document.degree["name"])
        self.assertEqual(data["organization"], incomplete_job_document.organization["name"])
        self.assertEqual(data["locations"], [location["name"] for location in incomplete_job_document.locations])
        self.assertIsNone(data.get("preferred_qualifications"))
        self.assertIsNone(data.get("minimum_qualifications"))
        self.assertIsNone(data.get("description"))
        self.assertIsNone(data.get("job_type"))
        self.assertIsNone(data.get("date_added"))
        self.assertIsNone(data.get("date_updated"))