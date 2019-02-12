import os
import re
from .strings import extractByRegex

NFS_HTTP_PREFIX = 'http://prme-vsanhol-observer-10.eng.vmware.com/vsanhol-nfs-vm/'
LOG_PATTERN = r'(.*VMWB-[A-Za-z0-9]{3}-4-VSANI-OCERT_\d+)'

def get_cert_base_link(text):
    if 'http' in text and not text.startswith(NFS_HTTP_PREFIX):
        return None
    return extractByRegex(LOG_PATTERN, text)

def nfs_get_text_from_link(link):
    if link.endswith('testdata.json'):
        return 'testdata.json'
    if link.endswith('testsummary.html'):
        return 'testsummary.html'
    if link.endswith('wiki.txt'):
        return 'wiki.txt'
    else:
        return os.path.basename(link)

def nfs_handler(link):
    nfs_links = ()
    cert_log_path = get_cert_base_link(link)

    if cert_log_path:
        test_data_path = os.path.join(cert_log_path, 'testdata.json')
        test_summary_path = os.path.join(cert_log_path, 'testsummary.html')
        wiki_txt_path = os.path.join(cert_log_path, 'wiki.txt')

        test_summary_wiki_link = '[{0} testsummary.html]'.format(test_summary_path)

        nfs_links = (
            {
                "title": test_summary_path,
                "subtitle": "testsummary.html url",
                "arg": test_summary_path
            },
            {
                "title": cert_log_path,
                "subtitle": "cert log base url",
                "arg": cert_log_path
            },
            {
                "title": test_data_path,
                "subtitle": "testdata.json url",
                "arg": test_data_path
            },
            {
                "title": wiki_txt_path,
                "subtitle": "wiki.txt url",
                "arg": wiki_txt_path
            },
            {
                "title": test_summary_wiki_link,
                "subtitle": "testsummary.html wiki link",
                "arg": test_summary_wiki_link
            },
        )
    
    return nfs_links
