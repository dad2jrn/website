import streamlit as st
from streamlit_lottie import st_lottie
import requests


st.set_page_config(
    page_title="Ron Meck | Senior Solutions Architect | Software Engineer",
    layout="wide",
)

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS
lottie_file = load_lottie("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


# HEADER SECTION
with st.container():
    st.subheader("Hi, I'm Ron Meck :wave:")
    st.title("Senior Solutions Architect and Software Engineer from Virginia.")
    st.write(
        """As an Sr. Software Engineering Manager/Enterprise Architect, I specialize in collaborating with designers, developers, and engineers to
            bring technical solutions to life. I am skilled at meeting with non- technical stakeholders regularly and explaining complex concepts in
            relatable terms. I make it a priority to stay up to date on business direction and processes to ensure that the solutions I design align with
            organizational objectives."""
    )
    st.write(
        """With my expertise in analyzing software that is not performing to expectations, I recommend solutions for improvements and architect
            serverless-first solutions utilizing ECS Fargate, Lambda, and DynamoDB cloud technologies. I am passionate about building impeccable
            software solutions to organizational deficiencies and collaborating with stakeholders to meet end-user requirements."""
    )
    st.write(
        """As a leader, I have led multiple teams of high-performing engineers to deliver on business intent and frequently present to senior leadership
        and business partners on technologies and roadmaps. I have also drafted design objectives and system design documents using Lucidchart, MS Visio,
        and gSuite."""
    )
    st.write(
        """I have extensive experience in developing enterprise solutions for modern systems and legacy applications. I have created application frameworks,
        codified procedures, and managed delivery processes, implementing strategic plans to maintain consistency with company guidelines and industry
        standards. I have also collected, outlined, and refined requirements, led design processes, and oversaw project progress."""
    )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """I am an Sr. Software Engineering Manager/Enterprise Architect, I specialize in collaborating with designers, developers, and engineers to
            bring technical solutions to life. I am skilled at meeting with non- technical stakeholders regularly and explaining complex concepts in
            relatable terms. I make it a priority to stay up to date on business direction and processes to ensure that the solutions I design align with
            organizational objectives."""
        )
    with right_column:
        st_lottie(lottie_file, height=300, key="coding")