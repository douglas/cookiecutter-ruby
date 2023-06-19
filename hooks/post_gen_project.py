#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def create_right_test_structure():
    """
    Create the right testing files according to the chosen test framework.
    """

    test_framework_to_use = '{{cookiecutter.test_framework_to_use|lower}}'

    if test_framework_to_use == 'minitest':
        test_directory = os.path.join(PROJECT_DIRECTORY, "test")
        example_test_file = os.path.join(PROJECT_DIRECTORY, "test_examples", "{{cookiecutter.project_slug}}_test.rb")
        test_helper_file = os.path.join(PROJECT_DIRECTORY, "test_examples", "test_helper.rb")

        os.mkdir(test_directory)
        shutil.copy(example_test_file, test_directory)
        shutil.copy(test_helper_file, test_directory)
    else:
        test_directory = os.path.join(PROJECT_DIRECTORY, "spec")
        example_spec_file = os.path.join(PROJECT_DIRECTORY, "test_examples", "{{cookiecutter.project_slug}}_spec.rb")

        os.mkdir(test_directory)
        shutil.copy(example_spec_file, test_directory)

    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, "test_examples"))

def set_execution_bit_on_main_file():
    main_file = os.path.join(PROJECT_DIRECTORY, "{{cookiecutter.project_slug}}.rb")
    os.chmod(main_file, 0o755)

create_right_test_structure()
set_execution_bit_on_main_file()
