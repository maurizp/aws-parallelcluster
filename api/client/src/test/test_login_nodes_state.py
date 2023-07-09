"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.7.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from assertpy import assert_that
import pytest
import pcluster_client
import re
from pcluster_client.model.login_nodes_state import LoginNodesState


class TestLoginNodesState(unittest.TestCase):
    """LoginNodesState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testValidLoginNodesState(self):
        LoginNodesState("active")

    def testInvalidLoginNodesState(self):
        with pytest.raises(
            BaseException,
            match=re.escape(r"Invalid value for `value` (invalid_value), "
                            r"must be one of ['pending', 'active', 'failed']")
        ):
            LoginNodesState("invalid_value")


if __name__ == '__main__':
    unittest.main()
