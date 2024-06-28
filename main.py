import streamlit as st
from streamlit_option_menu import option_menu
import functions.about as about
import functions.monitoring as monitor
import functions.ExploreMenue as expmenu
import functions.Simulation as sim
import functions.Config as config
import functions.Home as home


def menuconstructor():

    # 1. as sidebar menu
    st.set_page_config(layout="wide")
    with st.sidebar:
        select = option_menu("AgroPulse TwinHub", [ 'Monitoring' , 'Explore' , 'Simulation' , 'Configuration' , 'About'])

    if select == 'Monitoring':
        monitor.MonitorCreating()
    if select == 'About':
        about.homepageconstructor()
    if select == 'Simulation':
        sim.SimulationConstructor()
    if select == 'Configuration':
        config.ConstructorConfig()
    if select == 'About':
        home.homepageconstructor()
    if select == "Explore":
        expmenu.constructoemain()

if __name__ == '__main__':
    menuconstructor()
