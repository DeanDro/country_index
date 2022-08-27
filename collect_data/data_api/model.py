from flask_sqlalchemy import SQLAlchemy
from app import return_app

app = return_app()
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite://Countries.sqlite3'

db = SQLAlchemy(app)
class Countries(db.Model):

    """
    This is a class that represents all the details we want to store for a countr
    for our country ranking application. 
    """

    # Global variables 
    id = db.Column('country_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    worklife_balance = db.Column(db.Integer)
    safety_index = db.Column(db.Integer)
    family_friendly = db.Column(db.Integer)
    economic_strength = db.Column(db.Integer)
    access_healthcare = db.Column(db.Integer)
    overall_happiness = db.Column(db.Integer)
    gender_equality = db.Column(db.Integer)
    language_diff = db.Column(db.Integer)
    society_openess = db.Column(db.Integer)
    weather = db.Column(db.Integer)
    relocation_ease = db.Column(db.Integer)
    economic_future_prosperity = db.Column(db.Integer)
    education_quality = db.Column(db.Integer)
    perc_people_born_overseas = db.Column(db.Integer)
    access_education = db.Column(db.Integer)
    intern_companies = db.Column(db.Integer)
    top_universities = db.Column(db.Integer)
    social_stability = db.Column(db.Integer)
    innovation_levels = db.Column(db.Integer)
    tech_adaptability = db.Column(db.Integer)
    social_purpose = db.Column(db.Integer)
    forward_looking = db.Column(db.Integer)
    racial_equality = db.Column(db.Integer)
    avg_annual_income = db.Column(db.Integer)
    freedom_press = db.Column(db.Integer)
    national_heritage = db.Column(db.Integer)
    enterpren_levels = db.Column(db.Integer)
    green_energy_dev = db.Column(db.Integer)
    climate_policies = db.Column(db.Integer)
    proximity_popular_destinations = db.Column(db.Integer)
    lgbtq_friendly = db.Column(db.Integer)
    natural_environment = db.Column(db.Integer)
    population = db.Column(db.Integer)
    gdp_per_capita = db.Column(db.Integer)
    corruption_levels = db.Column(db.Integer)
    focus_development = db.Column(db.Integer)   # Nations commitment to overall development
    social_mobility = db.Column(db.Integer)
    focus_reducing_enequality = db.Column(db.Integer)
    global_liveability = db.Column(db.Integer)
    global_retirement = db.Column(db.Integer)
    per_popul_under_40 = db.Column(db.Integer)
    climate_change_impact = db.Column(db.Integer)
    national_debt = db.Column(db.Integer)
    proximity_hostile_ter = db.Column(db.Integer)
    unemployment_levels = db.Column(db.Integer)
    unemployment_18_24 = db.Column(db.Integer)

    