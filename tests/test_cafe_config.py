# -*- coding: utf-8 -*-


def test_help_message(testdir):
    result = testdir.runpytest(
        '--help',
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        'cafe-config:',
        '*--cafe-proj=CAFE_PROJ',
        '*Name of the project to test',
        '*--cafe-config=CAFE_CONFIG',
        '*Name of the Cafe configuration file for the project to'
    ])
