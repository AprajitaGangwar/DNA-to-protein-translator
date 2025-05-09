import streamlit as st
from PIL import Image

import streamlit as st


codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '', 'TAG': '',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
}

# Page title
st.title("DNA to Protein Translator App")

# Create two tabs
tab1, tab2 = st.tabs(["🧬 Translator Tool", "ℹ About"])

# TAB 1: Translator Tool
with tab1:
    st.header("DNA to Protein Translator")
    dna_input = st.text_input("Enter DNA sequence (A, T, G, C):", "ATGGCC")

    def translate_dna(dna):
        protein = ""
        dna = dna.upper()
        for i in range(0, len(dna), 3):
            codon = dna[i:i+3]
            if len(codon) == 3:
                protein += codon_table.get(codon, '?')  # '?' for unknown codons
        return protein

    if dna_input:
        protein_result = translate_dna(dna_input)
        st.write("Protein Sequence:", protein_result)

# TAB 2: About
with tab2:
    # Function to load image
    def load_image(image_file):
        return Image.open(image_file)

    # Home Page Content
    st.markdown("""
    *Welcome to translator application.*  
    - Converts DNA codons to amino acids using the genetic code.  
    - Supports translation in all three frames.  
    - Visual identification of ATG, TAA, TAG, TGA.  
    - Displays and allows export of the translated protein sequence.  
    - Option to translate reverse strand.
    """)

    st.markdown("---")

    # Team Section
    st.header("👨‍💻 Meet the Creator")
    col1, col2 = st.columns([1, 3])

    with col1:
        st.image(load_image("appy.jpg"), width=150)

    with col2:
        st.subheader("Aprajita Gangwar")
        st.write(
            """
            Hello ... I am Aprajita Gangwar, the creator of this app. I am passionate about bioinformatics and data science.  
            I enjoy learning new technologies and applying them to solve real-world problems. I also enjoy going on adventures and experiencing new destinations.  

            🔗 [LinkedIn](https://www.linkedin.com/in/aprajita-gangwar-086486251?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)  
            💻 [GitHub](https://github.com/AprajitaGangwar)
            """
        )

    st.markdown("---")

    # Acknowledgement Section
    st.header("🙏 Acknowledgement")
    st.info(
        """
        I would like to express my sincere gratitude to Dr. Kushagra Kashyap and Dr. Poonam Deshpande for their invaluable guidance, constant support, and encouragement throughout the course of this mini project.  
        Their expert insights and constructive suggestions greatly contributed to the successful completion of this work.  
        I am also thankful to all the faculty members and staff of the department for providing the necessary facilities and a conducive environment for learning and research.
        """
    )
