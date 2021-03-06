from unittest import TestCase
import os
import BeautifulSoup as bs

from phillyleg.management.scraper_wrappers import PhillyLegistarSiteWrapper

class LegistarTests (TestCase):
    
    def setUp(self):
        self.legfiles_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'testlegfiles'
        )
        self.pdfs_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'pdfs'
        )
        
    def test_RecognizeNotesRow(self):
        # The history on some filings (like key=73) have notes.  These need to
        # be detected.
        html = open(os.path.join(self.legfiles_dir, 'key73.html')).read()
        soup = bs.BeautifulSoup(html)
        
        wrapper = PhillyLegistarSiteWrapper()
        file_record, attachment_records, action_records, minutes_records = \
            wrapper.scrape_legis_file(73, soup)
        
        self.assertEqual(
            len([act_rec for act_rec in action_records
                 if act_rec['notes']]), 2)
    
    def test_ResolutionPdfParsesCorrectly(self):
        wrapper = PhillyLegistarSiteWrapper()
        expected_text = """ City of Philadelphia City of Philadelphia - 1 - City Council Chief Clerk's Office 402 City Hall Philadelphia, PA 19107 RESOLUTION NO. 110406 Introduced May 12, 2011 Councilmember DiCicco Referred to the Committee of the Whole RESOLUTION Appointing David Campoli to the Board of Directors of the Center City District. RESOLVED, BY THE COUNCIL OF THE CITY OF PHILADELPHIA, THAT David Campoli is hereby appointed as a member of the Board of Directors of the Center City District, to serve in a term ending December 31, 2012. City of Philadelphia RESOLUTION NO. 110406 continued City of Philadelphia - 2 - """

        # Raw stream
        resolution_pdf = open(os.path.join(self.pdfs_dir, '11530.pdf')).read()
        resolution_text = wrapper.extract_pdf_text(resolution_pdf)
        self.assertEqual(resolution_text, expected_text)
        
        # File URL
        resolution_pdf = 'file://' + os.path.join(self.pdfs_dir, '11530.pdf')
        resolution_text = wrapper.extract_pdf_text(resolution_pdf)
        self.assertEqual(resolution_text, expected_text)
        
        # Web URL
        resolution_pdf = 'http://legislation.phila.gov/attachments/11530.pdf'
        resolution_text = wrapper.extract_pdf_text(resolution_pdf)
        self.assertEqual(resolution_text, expected_text)
    
    def test_DealsWith404PdfAddressesCorrectly(self):
        # I don't know why they'd be deleting these files, but when they do (and
        # they do) we have to handle it.
        wrapper = PhillyLegistarSiteWrapper()
        expected_text = ''
        
        attachment_pdf = 'http://legislation.phila.gov/attachments/11595.pdf'
        attachment_text = wrapper.extract_pdf_text(attachment_pdf)
        self.assertEqual(attachment_text, expected_text)
