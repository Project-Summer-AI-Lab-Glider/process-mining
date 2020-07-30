import os
import sys
import logging

from xml.etree import ElementTree as tree
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver


BASE_URL = 'http://mail-archives.apache.org/mod_mbox/camel-dev/201704.mbox/browser'
