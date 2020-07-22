from datetime import datetime, timedelta
from django_dbq.models import Job
from django.urls import reverse
import json
from django_dbq_exports.models import Export
from django.test import TestCase
from django.utils.timezone import make_aware


class ExportModelTestCase(TestCase):
    
    def setUp(self):
        self.base_export = Export.objects.create(export_type='test_export')


    def test_create_initates_job(self):
        self.assertEqual(Job.objects.count(), 1)
        Export.objects.create(export_type='test_export')
        self.assertEqual(Job.objects.count(), 2)

    def test_subsequant_save_does_not_initiate_job(self):
        export = Export.objects.create(export_type='test_export')
        self.assertEqual(Job.objects.count(), 2)
        export.status_detail = "Changing the object"
        export.save()
        self.assertEqual(Job.objects.count(), 2)

    def test_update_status(self):
        self.assertEqual(self.base_export.status, Export.STATUS.QUEUED)
        self.base_export.update_status(Export.STATUS.FAILED, "Testing failure status update")
        self.base_export.refresh_from_db()
        self.assertEqual(self.base_export.status, Export.STATUS.FAILED)
        self.assertEqual(self.base_export.status_detail, "Testing failure status update")

    def test_calculate_run_time_with_started_and_completed(self):
        timedif = 3
        self.base_export.started = make_aware(datetime(2020, 6, 1, 12, 30, 0))
        self.base_export.completed = self.base_export.started + timedelta(seconds=timedif)
        self.base_export.save()
        self.assertEqual(self.base_export.runtime, timedif)

    def test_calculate_run_time_with_just_started(self):
        self.assertEqual(self.base_export.completed, None)
        self.base_export.started = make_aware(datetime(2020, 6, 1, 12, 30, 0))
        self.base_export.save()
        self.assertEqual(self.base_export.runtime, None)

    def test_str_return(self):
        self.assertEqual(str(self.base_export), str(self.base_export.id))


class DBQExportViewTestCase(TestCase):
    
    def setUp(self):
        self.base_export = Export.objects.create(export_type='test_export')

    def test_list_exports(self):
        response = self.client.get(reverse('dbq_export:dbq-export-list-create'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['id'], str(self.base_export.id))
    
    def test_retreive_single_export(self):
        response = self.client.get(reverse('dbq_export:dbq-export-retreive', kwargs={'pk': str(self.base_export.id)}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['id'], str(self.base_export.id))
    
    def test_create_export(self):
        self.assertEqual(Export.objects.count(), 1)

        export_data = {
            "export_type": "my_export",
            "export_params": {
                "length": 9
            }
        }

        response = self.client.post(
            reverse('dbq_export:dbq-export-list-create'),
            data=export_data,
            content_type='application/json'
        )

        print(response.json())
        print(response)
        print(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Export.objects.count(), 2)
        export = Export.objects.last()
        self.assertEqual(response.json()['id'], str(export.id))
        self.assertEqual(response.json()['export_type'], 'my_export')
        self.assertEqual(response.json()['export_params'], {'length': 9})

class BaseTaskTestCase(TestCase):

    def setUp(self):
        pass

    # Continue here
