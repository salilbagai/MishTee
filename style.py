mishtee_css = """
/* Core App Styling */
.gradio-container {
    background-color: #FAF9F6 !important;
    font-family: 'Inter', -apple-system, sans-serif !important;
}

/* Typography - High-End Serif for Headings */
h1, h2, h3 {
    font-family: 'Playfair Display', 'Georgia', serif !important;
    color: #333333 !important;
    letter-spacing: 0.05em !important;
    font-weight: 400 !important;
    text-transform: uppercase !important;
}

/* Body Text and Labels */
span, label, p {
    color: #333333 !important;
    font-weight: 300 !important;
    letter-spacing: 0.02em !important;
}

/* Sharp-Edged Buttons - Sober Terracotta */
button.primary {
    background-color: #C06C5C !important;
    color: white !important;
    border: 1px solid #C06C5C !important;
    border-radius: 0px !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    padding: 12px 24px !important;
    transition: all 0.3s ease !important;
    box-shadow: none !important;
}

button.primary:hover {
    background-color: transparent !important;
    color: #C06C5C !important;
    border: 1px solid #C06C5C !important;
}

/* Input Fields and Borders */
input, textarea, .step-container {
    border: 1px solid #D1D1D1 !important;
    border-radius: 0px !important;
    background-color: transparent !important;
    box-shadow: none !important;
}

/* Tables - Lightweight Sans-Serif */
table {
    font-family: 'Inter', sans-serif !important;
    font-weight: 300 !important;
    border-collapse: collapse !important;
}

th, td {
    border-bottom: 1px solid #E5E4E2 !important;
    padding: 15px !important;
    text-align: left !important;
}

/* Layout Padding and Spacing */
.gap {
    gap: 40px !important;
}

.block {
    margin-bottom: 30px !important;
    border: none !important;
    box-shadow: none !important;
}

/* Removing Bubbly Shapes */
* {
    border-radius: 0px !important;
}
"""
