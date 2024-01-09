import streamlit as st

st.set_page_config(
    page_title="Yuecheng Peng - HCI Researcher",
    page_icon="🥳",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.5, 0.5])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
          border-radius: 0;
    }
    </style>

    <div class="profile-img">

    ![](https://yuechengpeng.github.io/yuechengDesignGarden/resources/img/profile.jpg)
    </div>
    """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        # Yuecheng Peng
        
Hi, my name is Yuecheng Peng. I'm an HCI designer and developer.
        
🧑‍🔧 Doing all kinds of handworks is my favorite: fabricating tangible prototypes, exploring potential of various materials, etc.

📈 I also love to tell visual stories with data, offering insights and reflections of the society we live in.        

    """
    )

st.markdown(
    """
# Education
### University of Washington
<div style="display: flex; justify-content: space-between;">
    <span>Master of Science in Technology Innovation</span>
    <span>23.9 - 24.12</span>
</div>

### Zhejiang University
<div style="display: flex; justify-content: space-between;">
    <span>Bachelor of Engineering, Industrial Design</span>
    <span>19.9 - 23.6</span>
</div>

- **Grades**: GPA [3.98/4.0(91.93/100)] Rank [1/45]
- **Relevant Coursework**: Information Product Design, Information & Interaction Design Technology, Ergonomics
- **Awards**: Four times Excellent Academic Model, two times Second Class Scholarship, one time Third Class Scholarship

# Research Experience
### Fabrication of Smart Textiles
<div style="display: flex; justify-content: space-between;">
    <span>Project Leader & First Author</span>
    <span>@ Zhejiang University, 22.9 - 23.9</span>
</div>

- Conducted comprehensive material experiment and research.
- Physical prototyping using our proposed fabrication method.
- Write the paper independently (submitted to CHI24 as the first author).

### Designing Knowledge Graph Tool for Sustainability Education
<div style="display: flex; justify-content: space-between;">
    <span>Research Intern</span>
    <span>@ Zhejiang University, 21.10 - 22.4</span>
</div>

- Designed and developed a online knowledge graph tool ready to be used in sustainable education settings.
- Collected and organized related works of this research.
- Paper submitted to the journal of cleaner production.

### HoloLens2 Expander Interaction
<div style="display: flex; justify-content: space-between;">
    <span>Research Intern</span>
    <span>@ Zhejiang University, 21.8 - 21.12</span>
</div>

- Lead the design team, came up with design guidelines and standardized workflow, which increased the inter-team work
efficiency by 60%.
- Optimized user interaction experience with the Hololens2 interface and improved the comfort level as well as
immersiveness.
- Our design team was successfully selected to cooperate with Zhejiang Provincial Energy Group Company Ltd. in the
bidding.

### Music Emotion Visualization
<div style="display: flex; justify-content: space-between;">
    <span>Research Assistant</span>
    <span>@ Zhejiang University, 20.6 - 21.6</span>
</div>

- Responsible for literature research and functional design.
- Designed and conducted the experiment to collect people’s valence-arousal sentiment value on music as well as different
graphic and color expressions, which constitute the supporting database of our mobile App.
- This project was selected as a provincial research project (top 6%) and we developed a App demo.

# Skills
- **Programming**: Python, Frontend (HTML/CSS/JS), Arduino (C++), Unity (C#)
- **Prototyping**: Arduino, Raspberry Pi, CNC, laser-cutting, 3D printing, wood work




# Hobbies and Interests

🧝‍♂️ In my free time, I enjoy traveling around, especially stepping into the nature, because it abounds with fascinating creatures and will reward me with inspiration in designs.

# Interesting Projects
- [MagPaper: Rapid Prototyping of Haptic Interface Based on Pape](https://yuechengpeng.github.io/yuechengDesignGarden/magpaper.html)
    - Proposed a rapid prototyping method for creating accessible haptic interface.
    - Experimented with magnetic elastomer materials.
- [48°C SUGAR: Material Redesign of Traditional Sugar Figure Blowing Ar](https://yuechengpeng.github.io/yuechengDesignGarden/sugar.html)
    - Design of a new sugar material that allows hands-on interaction.
    - Conducted a user study to prove potentials of the proposed new material.
- [MOISTVALVE: A Moisture Sensory Soft Valve](https://yuechengpeng.github.io/yuechengDesignGarden/valve.html)
    - Prototyped a novel physical intelligent soft valve that can sense humidity without electricity.
    - Experimented with shape-changing responsive materials.
""",
        unsafe_allow_html=True,
)
