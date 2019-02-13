import unittest
import mock
import json
# from utest.helper import (write_json, read_json, remove_file)
from link.get_link import run

def get_run_result(query):
    result = run(query).get('items')
    sorted_result = sorted(result, key=lambda r: r.get('subtitle'))
    return sorted_result


class TestGetLink(unittest.TestCase):
    maxDiff = None

    def test_run_pr(self):
        expected_result_comment = [
            {
                "type": "file",
                "title": "PR 2231863#c11",
                "subtitle": "PR short description",
                "arg": "PR 2231863#c11",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11 PR 2231863#11]",
                "subtitle": "PR wiki link",
                "arg": "[https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11 PR 2231863#11]",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11",
                "subtitle": "full PR url",
                "arg": "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]

        pr_link_with_comment = "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863#c11"
        result = get_run_result(pr_link_with_comment)
        self.assertEqual(result, expected_result_comment)

        pr_link_with_comment = "2231863#c11"
        result = get_run_result(pr_link_with_comment)
        self.assertEqual(result, expected_result_comment)

        expect_result_without_comment = [
            {
                "type": "file",
                "title": "PR 2231863",
                "subtitle": "PR short description",
                "arg": "PR 2231863",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863 PR 2231863]",
                "subtitle": "PR wiki link",
                "arg": "[https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863 PR 2231863]",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863",
                "subtitle": "full PR url",
                "arg": "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]
        pr_link_without_comment = "https://bugzilla.eng.vmware.com/show_bug.cgi?id=2231863"
        result = get_run_result(pr_link_without_comment)
        self.assertEqual(result, expect_result_without_comment)

        pr_link_without_comment = "2231863"
        result = get_run_result(pr_link_without_comment)
        self.assertEqual(result, expect_result_without_comment)
    
    def test_run_confluence(self):
        # https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template
        # https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Cert+Review+Case+Study
        conf_full_display = "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template"
        conf_full_pages = "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Bugzilla+PR+Template"

        expected_result_pages = [
            {
                "type": "file",
                "title": "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Bugzilla+PR+Template",
                "subtitle": "confluence page url",
                "arg": "https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Bugzilla+PR+Template",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Bugzilla+PR+Template Bugzilla PR Template]",
                "subtitle": "confluence page wiki txt",
                "arg": "[https://confluence.eng.vmware.com/pages/viewpage.action?spaceKey=CERTSH&title=Bugzilla+PR+Template Bugzilla PR Template]",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "https://confluence.eng.vmware.com/display/CERTSH",
                "subtitle": "confluence space url",
                "arg": "https://confluence.eng.vmware.com/display/CERTSH",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]

        expected_result_display = [
            {
                "type": "file",
                "title": "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template",
                "subtitle": "confluence page url",
                "arg": "https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template Bugzilla PR Template]",
                "subtitle": "confluence page wiki txt",
                "arg": "[https://confluence.eng.vmware.com/display/CERTSH/Bugzilla+PR+Template Bugzilla PR Template]",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "https://confluence.eng.vmware.com/display/CERTSH",
                "subtitle": "confluence space url",
                "arg": "https://confluence.eng.vmware.com/display/CERTSH",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]

        result = get_run_result(conf_full_pages)
        # print(json.dumps(result, indent=4))
        self.assertEqual(result, expected_result_pages)
        
        result = get_run_result(conf_full_display)
        # print(json.dumps(result, indent=4))
        self.assertEqual(result, expected_result_display)

    def test_run_nfs(self):
        link = "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json"
        expected_result = [
            {
                "type": "file",
                "title": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714",
                "subtitle": "cert log base url",
                "arg": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/datalytics.json",
                "subtitle": "datalytics.json url",
                "arg": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/datalytics.json",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json",
                "subtitle": "testdata.json url",
                "arg": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testdata.json",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testsummary.html",
                "subtitle": "testsummary.html url",
                "arg": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testsummary.html",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testsummary.html testsummary.html]",
                "subtitle": "testsummary.html wiki link",
                "arg": "[http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/testsummary.html testsummary.html]",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/wiki.txt",
                "subtitle": "wiki.txt url",
                "arg": "http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/vsancert_logs/INT/all-flash/6_7_0/8169922/00050223/2018-07-03_22-15-35/VMWB-INT-4-VSANI-OCERT_1588451586290937714/wiki.txt",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]
        result = get_run_result(link)
        # print(json.dumps(result, indent=4))
        self.assertEqual(result, expected_result)
    
    def test_run_wiki(self):
        wiki_link = "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo"
        expected_result = [
            {
                "type": "file",
                "title": "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo",
                "subtitle": "wiki page url",
                "arg": "https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo TestInfo]",
                "subtitle": "wiki page wiki txt",
                "arg": "[https://wiki.eng.vmware.com/VSANCertification/VSANAnalytics/TestInfo TestInfo]",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]
        result = get_run_result(wiki_link)
        # print(json.dumps(result, indent=4))
        self.assertEqual(result, expected_result)
    
    def test_run_default(self):
        link = "google.com google"
        expected_result = [
            {
                "type": "file",
                "title": "google.com",
                "subtitle": "page url",
                "arg": "google.com",
                "icon": {
                    "path": "icon.png"
                }
            },
            {
                "type": "file",
                "title": "[google.com google]",
                "subtitle": "page wiki txt",
                "arg": "[google.com google]",
                "icon": {
                    "path": "icon.png"
                }
            }
        ]
        result = get_run_result(link)
        # print(json.dumps(result, indent=4))
        self.assertEqual(result, expected_result)
        