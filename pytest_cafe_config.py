# -*- coding: utf-8 -*-

import os

from cafe.configurator.managers import TestEnvManager
from cafe.common.reporting import cclogging
import pytest


def pytest_addoption(parser):
    group = parser.getgroup('cafe-config')
    group.addoption(
        '--cafe-proj',
        action='store',
        dest='cafe_proj',
        help='Name of the Cafe project'
    )

    group.addoption(
        '--cafe-config',
        action='store',
        dest='cafe_config',
        help='Name of the Cafe configuration file to use'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


def pytest_configure(config):
    test_env = TestEnvManager(
        config.getoption('cafe_proj'),
        config.getoption('cafe_config') + '.config',
        test_repo_package_name='tests')
    test_env.finalize()
    cclogging.init_root_log_handler()
    #self._log = cclogging.getLogger(
    #    cclogging.get_object_namespace(self.__class__))


@pytest.fixture
def bar(request):
    return request.config.option.cafe_proj
