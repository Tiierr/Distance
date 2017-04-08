# -*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators, BooleanField

from wtforms.validators import Required, Length
from wtforms.widgets.core import html_params
from wtforms.widgets import HTMLString

class InlineButtonWidget(object):
    """
    Render a basic ``<button>`` field.
    """
    input_type = 'submit'
    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault('value', field.label.text)
        return HTMLString('<button %s> Go!' % self.html_params(name=field.name, **kwargs))

class InlineSubmitField(BooleanField):
    """
    Represents an ``<button type="submit">``.  This allows checking if a given
    submit button has been pressed.
    """
    widget = InlineButtonWidget()

class SearchForm(FlaskForm):
    location = StringField('地理位置', validators=[Length(0,64),Required()])
    submit = InlineSubmitField()

class LatlngForm(FlaskForm):
    latlng = StringField('地理位置', validators=[Length(0,64),Required()])
    submit = InlineSubmitField()
