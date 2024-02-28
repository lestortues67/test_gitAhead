""" claire à 10h00 commit N°C3
Date : 27/02/2024 
Auteur : Christian Doriath 
Dossier : /Python39/MesDEv/Flask/Flask_codebase2023 
Fichier : app.py
Description : app "codebase" une base de données qui contient TOUTE notre base des connaissances
de code informatique. 
"""
 
#test pour utiliser gitAhead claire

import datetime
import string
from flask import Flask, request, render_template, session, redirect, url_for, flash, jsonify
from flask_bootstrap import Bootstrap


def mult_2(p_num):
    return p_num *10

def add_2(p_num):
    return p_num +10

def writer(p_text):
    print(p_text)