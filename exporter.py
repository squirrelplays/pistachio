from config import export_filepath, COLUMNS_TO_BLANK_BEFORE_EXPORT
import pandas as pd

def export_advanced_html(
    df,
    filename,
    columns,
    title="Data Table",
    row_filter=None,
    page_len=100
):
    """
    Export df[columns] to an HTML file with DataTables (using the searchbuilder extension).
    """
    working_df = df.copy()
    if row_filter is not None:
        working_df = working_df[row_filter].copy()

    working_df = working_df[columns]

    # Clean NaN values in configured columns for proper HTML sorting
    clean_cols = [c for c in COLUMNS_TO_BLANK_BEFORE_EXPORT if c in working_df.columns]
    working_df[clean_cols] = working_df[clean_cols].fillna("")

    # Define a safe formatter that leaves non-numeric values unchanged
    def safe_format(fmt_func):
        def wrapped(val):
            try:
                return fmt_func(val)
            except Exception:
                return val
        return wrapped

    # Apply baseball‑style formatting
    fmt = {}
    for col in working_df.columns:
        if col in ("best", "bestP", "war_hitting", "sp_war", "rp_war", "sp_warP", "rp_warP","DH", "C", "CF", "RF", "LF", "SS", "2B", "3B", "1B", "DHP", "1BP", "2BP", "3BP", "SSP", "LFP", "CFP", "RFP", "CP"):
            fmt[col] = safe_format("{:.1f}".format)
        elif col.endswith("_def"):
            fmt[col] = safe_format("{:.1f}".format)
        elif "wOBA" in col:
            fmt[col] = safe_format("{:.3f}".format)
        elif col in ("pWOBA", "pWOBAR", "pWOBAL"):
            fmt[col] = safe_format("{:.3f}".format)
        elif "wRC+" in col:
            fmt[col] = safe_format("{:.0f}".format)

    styled = working_df.style.format(fmt)
    html_table = styled.to_html(index=False, escape=False)
    # Ensure the table has the id DataTables expects:
    html_table = html_table.replace('<table ', '<table id="data" ', 1)

    full = HTML_DARK_TEMPLATE.format(
        title=title,
        table=html_table,
        page_len=page_len
    )
    path = export_filepath / filename
    with open(path, "w") as f:
        f.write(full)
    print(f"✅ Exported {title} → {path}")

def export_hitters(df):
    """
    Wrapper to export the hitters page.
    """
    cols = [
        "name", "org", "age", "pa", "best", "pos", "wRC+", "wOBA", "wOBAR", "wOBAL", "DH", "C", "CF", "RF", "LF", "SS", "2B", "3B", "1B", "wOBAP", "flag"
    ]
    filt = df["wOBA"] > 0.270
    export_advanced_html(
        df,
        filename="hitters.html",
        columns=cols,
        title="Hitters",
        row_filter=filt,
        page_len=100
    )

EXPORT_PAGES = [
    {
        "filename": "hitters.html",
        "title": "Hitters",
        "columns": [
            "name", "org", "minor", "age", "pa", "best", "bestP", "pos", "field", "wRC+", "wOBA", "wOBAR", "wOBAL", "wOBAP",
            "DH", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "C",  "flag"
        ],
        "filter": lambda df: df["wOBAP"] > 0.200,
        "page_len": 100
    },
    {
        "filename": "pitchers.html",
        "title": "Pitchers",
        "columns": [ 
            "name", "org", "minor", "age", "ip", "sp_war", "rp_war", "pwOBA", "pwOBAR", "pwOBAL", "sp_warP", "rp_warP", "pwOBAP", "flag"    
        ],
        "filter": lambda df: df["pwOBAP"] < 1.000,
        "page_len": 100
    },
    {
        "filename": "hit_prospects.html",
        "title": "Hitter prospects",
        "columns": [
            "name", "org", "minor", "age", "pa", "best", "bestP", "posP", "field", "wOBA", "wOBAR", "wOBAL", "wOBAP", "DHP", "1BP", "2BP", "3BP", "SSP", "LFP", "CFP", "RFP", "CP", "Cfram", "flag" 
        ],
        "filter": lambda df: df["wOBAP"] > 0.200,
        "page_len": 100
    },
    # More pages can be added here
]

def export_html_pages(df):
    """
    Export multiple pages using the EXPORT_PAGES definitions.
    """
    for page in EXPORT_PAGES:
        filt = page["filter"](df) if page.get("filter") else None
        export_advanced_html(
            df=df,
            filename=page["filename"],
            columns=page["columns"],
            title=page["title"],
            row_filter=filt,
            page_len=page.get("page_len", 100)
        )

# ------------------------------------------------------------------
# Advanced DataTables HTML export (dark theme, compact, SearchBuilder)
# ------------------------------------------------------------------

HTML_DARK_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>{title}</title>
  <!-- DataTables core & extensions -->
  <link rel="stylesheet" href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css"/>
  <link rel="stylesheet" href="https://cdn.datatables.net/searchbuilder/1.4.0/css/searchBuilder.dataTables.min.css"/>
  <link rel="stylesheet" href="https://cdn.datatables.net/fixedheader/3.3.2/css/fixedHeader.dataTables.min.css"/>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet"/>
  <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
  <script src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
  <script src="https://cdn.datatables.net/searchbuilder/1.4.0/js/dataTables.searchBuilder.min.js"></script>
  <script src="https://cdn.datatables.net/fixedheader/3.3.2/js/dataTables.fixedHeader.min.js"></script>

  <style>
    /* ----- Dark theme & compact table ----- */
    body {{
      background:#1c1c1c; color:#e0e0e0; margin:0; padding:1rem; font-family:Arial,Helvetica,sans-serif;
      font-family: 'Roboto', sans-serif;
    }}
    table.dataTable {{
      background:#1c1c1c; color:#e0e0e0; font-size:0.8rem;
      font-family: 'Roboto', sans-serif;
    }}
    /* zebra striping with dark tones */
    table.dataTable tbody tr:nth-child(odd)  {{ background:#262626; }}
    table.dataTable tbody tr:nth-child(even) {{ background:#1e1e1e; }}
    /* subtle hover effect */
    table.dataTable tbody tr:hover {{ background: rgba(255,255,255,0.05); }}
    /* header */
    table.dataTable thead th {{
      background:#2f2f2f; color:#e0e0e0;
      box-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }}

    /* inline top controls (search builder, length, filter) */
    #data-searchBuilderContainer,
    div.dataTables_length,
    div.dataTables_filter {{
      display: inline-block;
      vertical-align: middle;
      margin-right: 1rem;
    }}
    /* remove "Custom Search Builder" title */
    #data-searchBuilderContainer .dtsb-header {{
      display: none;
    }}
    /* hide the SearchBuilder title text */
    #data-searchBuilderContainer .dtsb-title {{
      display: none !important;
    }}

    /* style length selector and search input for visibility */
    div.dataTables_length label,
    div.dataTables_filter label {{
      color: #e0e0e0;
    }}
    div.dataTables_length select,
    div.dataTables_filter input {{
      color: #e0e0e0;
      background: #2f2f2f;
      border: none;
    }}
    /* header row layout */
    .header-row {{
      display: flex;
      align-items: center;
      font-size: 1rem;
      margin-bottom: 1rem;
    }}
    .header-row h2 {{
      margin: 0;
      font-size: 1rem;
      font-weight: normal;
      color: #e0e0e0;
    }}
    #header-controls {{
      margin-left: 1rem;
    }}
  </style>
</head>
<body>
  <div class="header-row">
    <h2>{title}</h2>
    <div id="header-controls"></div>
  </div>
  {table}
<script>
$.fn.dataTable.ext.order['numeric-empty-last-asc'] = function(settings, col) {{
    return this.api().column(col, {{order:'index'}}).nodes().map(function(td) {{
        var v = parseFloat($(td).text());
        return isNaN(v) ? Infinity : v;
    }});
}};
$.fn.dataTable.ext.order['numeric-empty-last-desc'] = function(settings, col) {{
    return this.api().column(col, {{order:'index'}}).nodes().map(function(td) {{
        var v = parseFloat($(td).text());
        return isNaN(v) ? -Infinity : v;
    }});
}};
$(document).ready(function(){{
    var ascCols = ['pwOBA','pwOBAR','pwOBAL'];
    var descCols = ['sp_war','rp_war'];
    var numDefs = ascCols.map(function(name) {{
        return {{
            targets: $('#data thead th').filter(function() {{ return $(this).text() === name; }}).index(),
            orderDataType: 'numeric-empty-last-asc',
            orderSequence: ['asc','desc']
        }};
    }}).concat(descCols.map(function(name) {{
        return {{
            targets: $('#data thead th').filter(function() {{ return $(this).text() === name; }}).index(),
            orderDataType: 'numeric-empty-last-desc',
            orderSequence: ['desc','asc']
        }};
    }}));
  $('#data').DataTable({{
      dom: 'Qlfrtip',            // Q = SearchBuilder, l = length selector, f = search bar, r = processing, t = table, i = info, p = paging
      pageLength: {page_len},
      ordering: true,
      searching: true,
      paging: true,
      fixedHeader: true,
      stripeClasses: ['odd', 'even'],
      searchBuilder: {{ }},
      columnDefs: [ {{ targets: 0, visible: false }} ].concat(numDefs)
  }});
      // move SearchBuilder UI into header controls
      $('#data-searchBuilderContainer').appendTo('#header-controls');
      // rename the add button
      $('.dtsb-add').text('Add search filter');
}});
</script>
</body>
</html>
"""