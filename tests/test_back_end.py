import unittest
from flask_testing import TestCase
from application import app, db
from os import getenv
from flask import render_template, redirect, url_for, request
from application.models import characters, classes

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLE=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        example = characters(name = "Testchar",                
                clas = "Fighter",
                race = "Human",
                level = 5,
                CON = 16,
                DEX = 15,
                STR = 14,
                INT = 13,
                WIS = 12,
                CHA = 11,
                Health = 50,
                Armor = 19,
                Spell_points = 0,
                Speed = 30)

        db.session.add(example)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase): #all these tests are just calling the pages to see if they load. dynamic url pages use identity=1 so they can use the character created in setUp

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_sheet_view(self):
        response = self.client.get(url_for('sheet', identity=1))
        self.assertEqual(response.status_code, 200)

    def test_new_view(self):
        response = self.client.get(url_for('new'))
        self.assertEqual(response.status_code, 200)

    def test_edit_view(self):
        response = self.client.get(url_for('edit', identity=1))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_view(self):
        response = self.client.get(url_for('delete', identity=1))
        self.assertEqual(response.status_code, 200)



class TestFunctionality(TestBase):

    def test_new_char(self):
        with self.client:
            start = characters.query.count() #num of characters in db at start is equal to 1
            response = self.client.post(
                '/new',
                data=dict(
                name = "Testing",
                clas = "Wizard",
                race = "Elf",
                level = 5,
                CON = 16,
                DEX = 15,
                STR = 14,
                INT = 13,
                WIS = 12,
                CHA = 11,
                Health = 50,
                Armor = 19,
                Spell_points = 100,
                Speed = 30
                ),
                follow_redirects=True
            )
            end = characters.query.count() #num of characters in db after creation of a character, should be equal to 2
            self.assertTrue(end > start) #check if creation has gone through

    def test_update_char(self):
        with self.client:
            start = characters.query.filter_by(id=1).first().name #name @id=1 at start
            response = self.client.post(
                    url_for("edit", identity=1),
                    data=dict(
                    name = "Changed", #change name from Testchar to Changed, all other info is identical
                    clas = "Fighter",
                    race = "Human",
                    level = 5,
                    CON = 16,
                    DEX = 15,
                    STR = 14,
                    INT = 13,
                    WIS = 12,
                    CHA = 11,
                    Health = 50,
                    Armor = 19,
                    Spell_points = 0,
                    Speed = 30),
                    follow_redirects=True)
            end = characters.query.filter_by(id=1).first().name #name @id=1 after update
            self.assertTrue(end != start) #check if update has gone through

    def test_delete_char(self):
        with self.client:
            start = characters.query.count() #num of entries in db
            response = self.client.post(
                    url_for("delete", identity=1),
                    follow_redirects=True)
            end = characters.query.count() #num of entries in db after deletion
            self.assertTrue(start > end) #check if delete has gone through
