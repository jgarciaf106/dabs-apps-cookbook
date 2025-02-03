import streamlit as st
from view_groups import groups

st.markdown(
    """
    **Welcome to the Databricks Apps Cookbook!**

    Are you ready to serve some tasty apps to your users? You're in the right place!  
    
    Explore the recipes via the sidebar to quickly build flexible and engaging data apps directly on Databricks.

    Have a great recipe to share? Raise a pull request on the [GitHub repository](https://github.com/pbv0/databricks-apps-cookbook)!
    """
)

st.header("Recipes", divider=True)

groups = [group for group in groups if group.get("title")]

for i in range(0, len(groups), 4):
    row_groups = groups[i : i + 4]
    # Always create 4 columns
    cols = st.columns(4)
    for col, group in zip(cols, row_groups):
        with col:
            with st.container(border=True):
                st.markdown(f"**{group['title']}**")
                for view in group["views"]:
                    st.page_link(
                        page=view["page"], label=view["label"], help=view["help"]
                    )

st.header("Links", divider=True)
col_a, col_b, col_c = st.columns(3)

with col_a:
    st.markdown(
        """
        #### Official documentation
        - [AWS](https://docs.databricks.com/en/dev-tools/databricks-apps/index.html)
        - [Azure](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/)
        - [Python SDK](https://databricks-sdk-py.readthedocs.io/en/latest/)
        """
    )

with col_b:
    st.markdown(
        """
        #### Code samples
        - [Databricks Apps Templates](https://github.com/databricks/app-templates)
        """
    )

with col_c:
    st.markdown(
        """
        #### Blog posts
        - [Databricks Apps with React and FastAPI](https://www.linkedin.com/pulse/building-data-applications-databricks-apps-ivan-trusov-6pjwf/)
        """
    )
