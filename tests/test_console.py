#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from unittest.mock import create_autospec
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO
import sys
import unittest
""""Unittest Module for console.py"""


class TestConsole(unittest.TestCase):
    '''Unittest for console.py module'''

    def setUp(self):
        ''' setting the mock_stdout and mock_stdin'''
        self.mock_stdout = create_autospec(sys.stdout)
        self.mock_stdin = create_autospec(sys.stdin)

    def test_console(self, server=None):
        ''' instatiates Console for HBNBCommand '''
        self.mock_stdout = create_autospec(sys.stdout)
        self.mock_stdin = create_autospec(sys.stdin)
        return HBNBCommand(stdout=self.mock_stdout, stdin=self.mock_stdin)

    def test_Quit(self):
        """tests quit method"""

        cmd = HBNBCommand()
        self.assertRaises(SystemExit, quit)

    def test_docs(self):
        """ tests docstrings """
        self.assertTrue(len(HBNBCommand.__doc__) > 0,
                "** There is No docstring Found **")
        """Check for docstring existance"""
    def test_docstrings_in_console(self):
        """Test docstrings exist in console.py"""
        self.assertTrue(len(HBNBCommand.__doc__) >= 1)

    """Test command interpreter outputs"""
    def test_emptyline(self):
        """Test without any user input"""
        with patch('sys.stdout' , new=StringIO()) as fake_output:
            HBNBCommand().onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Test cmd output: create"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n",
                    fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            HBNBCommand().onecmd("create someClass")
            self.assertEqual("** class doesn't exist **\n",
                    fake_output.getvalue())

    def test_show_id(self):
        ''' test show id '''
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_destroy_empty(self):
        ''' test destroy method '''
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(v.getvalue() == "** class name missing **\n")

    def test_class_exist(self):
        ''' test class name exist '''
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(v.getvalue() == "** class doesn't exist **\n")

    def test_all(self):
        ''' test all the method '''
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_update(self):
        ''' test the update method '''
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout' , new=StringIO()) as v:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(v.getvalue() == "** instance id missing **\n")

    def test_alt_all(self):
        ''' test [class].all method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(v.getvalue()) > 0)

    def test_count(self):
        ''' test [class].count method '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(int(v.getvalue()) >= 0)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as v:
            self.assertTrue(int(v.getvalue()) >= 1)

    def test_user(self):
        ''' Test the user object using the console. '''
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('create User')
            user_id = v.getvalue()
            self.assertTrue(user_id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('show User')
            self.assertTrue(v.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd('all User')
            self.assertTrue(v.getvalue() != "** class doesnt exist **\n")
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("update User" + user_id + "name betty")
            HBNBCommand().onecmd("show User" + user_id)
            self.assertFalse("betty" in v.getvalue())
            HBNBCommand().onecmd("destroy user" + user_id)
        with patch('sys.stdout', new=StringIO()) as v:
            HBNBCommand().onecmd("show User" + user_id)
            self.assertEqual(v.getvalue() != "** no instance found **\n")

    if __name__ == '__main__':
        unittest.main()
