#******************************************************************************
#
# Copyright (c) 2016 Microsoft Corporation. All rights reserved.
#
# This code is licensed under the MIT License (MIT).
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# // LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#******************************************************************************


import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SimpleCalculatorTests(unittest.TestCase):

    @classmethod

    def setUpClass(self):
        #set up appium
        desired_caps = {}

        desired_caps["app"] = "C:\\Users\\taimu\\AppData\\Local\\Programs\\ui.ep.launcher\\AAI-EP.exe"
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities= desired_caps)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    

    def test_1_CreateT(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name(" CREATE TEST").is_enabled()
        self.driver.find_element_by_name(" CREATE TEST").click()
        self.driver.find_element_by_name("Endurance Test").is_enabled()
        self.driver.find_element_by_name("Endurance Test").click()
        self.driver.find_element_by_name("NEXT STEP").click()
        self.driver.find_element_by_name("NEXT STEP").click()
        self.driver.find_element_by_name("AAI Ego").click()
        self.driver.find_element_by_name("NEXT STEP").click()
        self.driver.implicitly_wait(100)
        self.driver.find_element_by_name("START TEST GENERATION").click()
        self.driver.find_element_by_name('START')
        self.driver.find_element_by_name("START").click()
        self.driver.implicitly_wait(5000)

    # def test_2_Export(self):
    #     self.driver.implicitly_wait(5000)
    #     self.driver.find_element_by_name("Endurance Test").is_enabled()
    #     self.driver.find_element_by_name("Endurance Test").click()
    #     self.driver.find_element_by_name("EXPORT").is_enabled()
    #     self.driver.find_element_by_name("EXPORT")
    #     self.driver.implicitly_wait(5000)

    def test_3_Archive(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name("ANALYZE").is_enabled()
        self.driver.find_element_by_name("ANALYZE").click()
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name("ARCHIVE").is_enabled()
        self.driver.find_element_by_name("ARCHIVE").click()

    def test_4_StopExecution(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name("STOP").is_enabled()
        self.driver.find_element_by_name("STOP").click()
        self.driver.implicitly_wait(5000)

    def test_5_LeaveQue(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name("LEAVE QUEUE").is_enabled()
        self.driver.find_element_by_name("LEAVE QUEUE").click()
        self.driver.implicitly_wait(5000)

    def test_6_ArchivedTests(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_1").is_enabled()
        self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_1").click()
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_name("Archived Tests")
        self.driver.find_element_by_name("MORE")

    # def test_6_ArchivedTests(self):
    #     self.driver.implicitly_wait(5000)
    #     self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_1").is_enabled()
    #     self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_1").click()
    #     self.driver.implicitly_wait(5000)
    #     self.driver.find_element_by_name("Archived Tests")
    #     self.driver.find_element_by_name("MORE")
    #     self.driver.find_element_by_name("MORE").click()
    #     self.driver.find_element_by_name()
        
    def test_7_ScenarioLibrary(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_2").is_enabled()
        self.driver.find_element_by_accessibility_id("sidebar-image_menuitem_2").click()
        self.driver.find_elements_by_name("IMPORT SCENARIO") 

    def test_8_AAIlogo(self):
        self.driver.implicitly_wait(5000)
        self.driver.find_element_by_accessibility_id("sidebar-logo").is_enabled()
        self.driver.find_element_by_accessibility_id("sidebar-logo")
    


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleCalculatorTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
