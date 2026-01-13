import streamlit as st

st.set_page_config(layout="wide")
st.title("Chacho Draft Coach")
st.write("Engine v1.0 — Online")

import yaml
import streamlit as st

def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

try:
    brawlers = load_yaml("data/brawlers.yaml")
    maps = load_yaml("data/maps.yaml")
    tiers = load_yaml("data/tiers.yaml")
    rules = load_yaml("data/rules.yaml")
    meta = load_yaml("data/meta.yaml")

    st.success("✅ Datos cargados correctamente")

except Exception as e:
    st.error("❌ Error cargando datos")
    st.exception(e)
