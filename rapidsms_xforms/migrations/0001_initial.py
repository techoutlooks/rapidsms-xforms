# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.manager
import eav.fields
from django.conf import settings
import django.contrib.sites.managers


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
        ('eav', '__first__'),
        ('rapidsms', '0006_auto_20150722_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('binary', models.FileField(upload_to=b'binary')),
            ],
        ),
        migrations.CreateModel(
            name='XForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Human readable name.', max_length=32)),
                ('keyword', eav.fields.EavSlugField(help_text=b'The SMS keyword for this form, must be a slug.', max_length=32)),
                ('description', models.TextField(help_text=b'The purpose of this form.', max_length=255)),
                ('response', models.CharField(help_text=b'The response sent when this form is successfully submitted.', max_length=255)),
                ('active', models.BooleanField(default=True, help_text=b'Inactive forms will not accept new submissions.')),
                ('command_prefix', models.CharField(default=b'+', choices=[(b'+', b'Plus (+)'), (b'-', b'Dash (-)')], max_length=1, blank=True, help_text=b"The prefix required for optional field commands, defaults to '+'", null=True)),
                ('keyword_prefix', models.CharField(blank=True, max_length=1, null=True, help_text=b'The prefix required for form keywords, defaults to no prefix.', choices=[(b'+', b'Plus (+)'), (b'-', b'Dash (-)')])),
                ('separator', models.CharField(blank=True, max_length=1, null=True, help_text=b'The separator character for fields, field values will be split on this character.', choices=[(b',', b'Comma (,)'), (b';', b'Semicolon (;)'), (b':', b'Colon (:)'), (b'*', b'Asterisk (*)')])),
                ('restrict_message', models.CharField(help_text=b'The error message that will be returned to users if they do not have the right privileges to submit this form.  Only required if the field is restricted.', max_length=160, null=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('restrict_to', models.ManyToManyField(help_text=b'Restrict submissions to users of this group (if unset, anybody can submit this form)', to='auth.Group', blank=True)),
                ('site', models.ForeignKey(to='sites.Site')),
            ],
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='XFormField',
            fields=[
                ('attribute_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='eav.Attribute')),
                ('field_type', models.SlugField(max_length=8, null=True, blank=True)),
                ('command', eav.fields.EavSlugField(max_length=32)),
                ('order', models.IntegerField(default=0)),
                ('xform', models.ForeignKey(related_name='fields', to='rapidsms_xforms.XForm')),
            ],
            options={
                'ordering': ('order', 'id'),
            },
            bases=('eav.attribute',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='XFormFieldConstraint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=10, choices=[(b'min_val', b'Minimum Value'), (b'max_val', b'Maximum Value'), (b'min_len', b'Minimum Length'), (b'max_len', b'Maximum Length'), (b'req_val', b'Required'), (b'regex', b'Regular Expression')])),
                ('test', models.CharField(max_length=255, null=True)),
                ('message', models.CharField(max_length=160)),
                ('order', models.IntegerField(default=1000)),
                ('field', models.ForeignKey(related_name='constraints', to='rapidsms_xforms.XFormField')),
            ],
        ),
        migrations.CreateModel(
            name='XFormSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=8, choices=[(b'www', b'Web Submission'), (b'sms', b'SMS Submission'), (b'odk-www', b'ODK Web Submission'), (b'odk-sms', b'ODK SMS Submission'), (b'import', b'Imported Submission')])),
                ('raw', models.TextField()),
                ('has_errors', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('confirmation_id', models.IntegerField(default=0)),
                ('connection', models.ForeignKey(to='rapidsms.Connection', null=True)),
                ('xform', models.ForeignKey(related_name='submissions', to='rapidsms_xforms.XForm')),
            ],
        ),
        migrations.CreateModel(
            name='XFormSubmissionValue',
            fields=[
                ('value_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='eav.Value')),
                ('submission', models.ForeignKey(related_name='values', to='rapidsms_xforms.XFormSubmission', null=True)),
            ],
            bases=('eav.value',),
        ),
    ]
