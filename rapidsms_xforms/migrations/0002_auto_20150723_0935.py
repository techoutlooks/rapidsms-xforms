# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rapidsms_xforms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xformsubmissionvalue',
            name='submission',
            field=models.ForeignKey(related_name='values', default=None, to='rapidsms_xforms.XFormSubmission'),
            preserve_default=False,
        ),
    ]
