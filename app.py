import streamlit as st

st.set_page_config(page_title="Emmanuel Makinde Portfolio", layout="wide")

# Header
st.title("Emmanuel Makinde")
st.subheader("Graduate Student in Robotics | Software Engineer")
st.write("Seattle, WA")
st.write("makindee@uw.edu |  857-269-9062")

# Sidebar Navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Education", "Skills", "Projects", "Experience", "Activities"])

# Education
if selection == "Education":
    st.header(" Education")
    st.markdown("**University of Washington**  \nMS in Technology Intelligence (Robotics) — *Expected March 2026*")
    st.markdown("**Wentworth Institute of Technology**  \nBS in Computer Science")

# Skills
elif selection == "Skills":
    st.header(" Skills")
    st.markdown("**Software:** Eclipse, PyCharm, Spyder, AutoCAD, Corel Draw, SolidWorks")
    st.markdown("**Programming:** Python, Java, HTML, JavaScript")
    st.markdown("**Operating Systems:** Windows, macOS")

# Projects
elif selection == "Projects":
    st.header("💡 Projects")
    st.subheader("DNA Sequencing Site")
    st.write("Java-based comparison tool for finding the longest DNA string match.")
    
    st.subheader("2D Pacman Game")
    st.write("Java & JavaFX implementation of a custom Pacman with original rules and graphics.")

# Experience
elif selection == "Experience":
    st.header("Experience")

    st.subheader("Software Engineering Intern")
    st.caption("Enlabel Global Services, Boston — 2023")
    st.markdown("- Maintained internal applications")
    st.markdown("- Utilized AWS EC2 and CloudWatch")
    st.markdown("- Improved code logic and documentation")

    st.subheader("Gym Trainer")
    st.caption("Wentworth Fitwell — 2022–2024")

    st.subheader("Mentor & Library Assistant")
    st.caption("Wentworth — 2021–2022")

    st.subheader("Tech Manager")
    st.caption("Appletree Nigeria Ltd — 2016–2018")

# Activities
elif selection == "Activities":
    st.header("Activities & Memberships")
    st.markdown("- National Society of Black Engineers (NSBE) Member")
    st.markdown("- Vice President, WASU (2022–2024)")
    st.markdown("- Rugby Team Member, Wentworth")

# Footer
st.markdown("---")
st.markdown("© 2025 Emmanuel Makinde")
