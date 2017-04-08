# -*- coding:utf-8 -*-
from flask import request, render_template, session,flash, redirect, url_for, current_app, abort
from flask_googlemaps import Map
from .forms import SearchForm, LatlngForm
from ..distance import Distance, GoogleDistance
from ..util import ListToString
from . import main

@main.route('/',methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        location = form.location.data
        distance = Distance(location)
        if distance.status == '404':
            abort(404)
        relatlng =  distance.relatlng
        latlng = distance.latlng
        return redirect(url_for('.mapview', latlng=latlng + relatlng))
    return render_template('index.html', form=form)

@main.route("/map/<list:latlng>",methods=['POST', 'GET'])
def mapview(latlng):
    form = SearchForm()
    if form.validate_on_submit():
        location = form.location.data
        distance = Distance(location)
        if distance.status == '404':
            abort(404)
        relatlng =  distance.relatlng
        latlng = distance.latlng
        return redirect(url_for('.mapview', latlng=latlng + relatlng))
    home = Map(
        identifier="home",
        lat=latlng[0],
        lng=latlng[1],
        markers=[
          {
             'lat': latlng[0],
             'lng': latlng[1],
             'infobox': ListToString(latlng[:2]).toString()
          },
        ]
    )

    destination = Map(
        identifier="destination",
        lat=latlng[2],
        lng=latlng[3],
        markers=[
          {
             'lat': latlng[2],
             'lng': latlng[3],
             'infobox': ListToString(latlng[2:]).toString()
          },
        ]
    )
    return render_template('map.html', home=home, destination=destination, form=form)

@main.route('/googlemap',methods=['POST', 'GET'])
def googlemap_index():
    form = SearchForm()
    if form.validate_on_submit():
        location = form.location.data
        distance = GoogleDistance(location)
        if distance.status == 'ZERO_RESULTS':
            abort(404)
        relatlng =  distance.relatlng
        latlng = distance.latlng
        return redirect(url_for('.googlemapview', latlng=latlng + relatlng))
    return render_template('gm_index.html', form=form)

@main.route("/googlemap/<list:latlng>",methods=['POST', 'GET'])
def googlemapview(latlng):
    form = SearchForm()
    if form.validate_on_submit():
        location = form.location.data
        distance = GoogleDistance(location)
        if distance.status == 'ZERO_RESULTS':
            abort(404)
        relatlng =  distance.relatlng
        latlng = distance.latlng
        return redirect(url_for('.googlemapview', latlng=latlng + relatlng))
    home = Map(
        identifier="home",
        lat=latlng[0],
        lng=latlng[1],
        markers=[
          {
             'lat': latlng[0],
             'lng': latlng[1],
             'infobox': ListToString(latlng[:2]).toString()
          },
        ]
    )

    destination = Map(
        identifier="destination",
        lat=latlng[2],
        lng=latlng[3],
        markers=[
          {
             'lat': latlng[2],
             'lng': latlng[3],
             'infobox': ListToString(latlng[2:]).toString()
          },
        ]
    )
    return render_template('gmap.html', home=home, destination=destination, form=form)

@main.route('/latlng',methods=['POST', 'GET'])
def latlng_index():
    form = LatlngForm()
    if form.validate_on_submit():
        latlng = list(map(float, form.latlng.data.split(',')))
        return redirect(url_for('.latlngview', latlng=latlng))
    return render_template('latlng_index.html', form=form)

@main.route("/latlng/<list:latlng>",methods=['POST', 'GET'])
def latlngview(latlng):
    form = LatlngForm()
    if form.validate_on_submit():
        latlng = list(map(float, form.latlng.data.split(',')))
        return redirect(url_for('.latlngview', latlng=latlng))
    home = Map(
        identifier="home",
        lat=latlng[0],
        lng=latlng[1],
        markers=[
          {
             'lat': latlng[0],
             'lng': latlng[1],
             'infobox': ListToString(latlng).toString()
          },
        ]
    )
    return render_template('latlng.html', home=home, form=form)
