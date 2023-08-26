#!/usr/bin/env python3
"""test the client module"""

import unittest
from unittest.mock import MagicMock, patch
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """Tests the GithubOrgClient class"""
    @parameterized.expand([
        ("goggle", {"login": "goggle"}),
        ("abc", {"login": "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fn: MagicMock) -> None:
        """Tests the org method"""
        mocked_fn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
