from data.create_dummy_data import create_dummy_data
from UI.login_page_UI import run_login_UI

#will create some books if book_data.json or reader_data.json files doen't exist yet
create_dummy_data()

run_login_UI()