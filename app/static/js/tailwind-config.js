tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#650006",
        "primary-container": "#8f000d",
        "primary-fixed": "#ffdad6",
        "primary-fixed-dim": "#ffb4ac",
        "on-primary": "#ffffff",
        "on-primary-container": "#ff958b",
        "on-primary-fixed": "#410003",
        "on-primary-fixed-variant": "#92030f",
        "inverse-primary": "#ffb4ac",

        "secondary": "#705a4c",
        "secondary-container": "#f8dac8",

        "background": "#fbfbe2",
        "surface": "#fff8f5",
        "surface-bright": "#fbfbe2",
        "surface-dim": "#dbdcc3",
        "surface-variant": "#e4e4cc",
        "surface-tint": "#b52524",
        "surface-container": "#efefd7",
        "surface-container-low": "#f5f5dc",
        "surface-container-lowest": "#ffffff",
        "surface-container-high": "#eaead1",
        "surface-container-highest": "#e4e4cc",

        "on-background": "#1b1d0e",
        "on-surface": "#1b1d0e",
        "on-surface-variant": "#5a403e",

        "inverse-surface": "#303221",
        "inverse-on-surface": "#f2f2d9",

        "outline": "#8e706d",
        "outline-variant": "#e2beba",

        "error": "#ba1a1a",
        "error-container": "#ffdad6",
        "on-error": "#ffffff",
        "on-error-container": "#93000a",
      },
      borderRadius: {
        DEFAULT: "0.25rem",
        lg: "0.5rem",
        xl: "0.75rem",
        full: "9999px"
      },
      spacing: {
        "xs": "4px",
        "sm": "8px",
        "base": "8px",
        "md": "16px",
        "gutter": "20px",
        "lg": "24px",
        "xl": "32px",
        "xxl": "48px",
        "margin-mobile": "20px",
        "margin-desktop": "64px",
        "container-margin": "20px",
        "touch-target-min": "48px",
        "container-max": "1200px"
      },
      fontFamily: {
        "display-lg": ["Newsreader"],
        "display-lg-mobile": ["Newsreader"],
        "headline-lg": ["Newsreader"],
        "headline-lg-mobile": ["Newsreader"],
        "headline-md": ["Newsreader"],
        "headline-sm": ["Newsreader"],
        "body-lg": ["Be Vietnam Pro"],
        "body-md": ["Be Vietnam Pro"],
        "label-lg": ["Be Vietnam Pro"],
        "label-sm": ["Be Vietnam Pro"],
        "label-md": ["Be Vietnam Pro"]
      },
      fontSize: {
        "display-lg": ["48px", { lineHeight: "56px", letterSpacing: "-0.02em", fontWeight: "700" }],
        "headline-lg": ["32px", { lineHeight: "40px", fontWeight: "600" }],
        "headline-lg-mobile": ["28px", { lineHeight: "36px", fontWeight: "600" }],
        "headline-md": ["24px", { lineHeight: "32px", fontWeight: "500" }],
        "headline-sm": ["24px", { lineHeight: "32px", fontWeight: "600" }],
        "body-lg": ["18px", { lineHeight: "28px", fontWeight: "400" }],
        "body-md": ["16px", { lineHeight: "24px", fontWeight: "400" }],
        "label-lg": ["14px", { lineHeight: "20px", letterSpacing: "0.05em", fontWeight: "600" }],
        "label-sm": ["12px", { lineHeight: "16px", fontWeight: "500" }],
        "label-md": ["12px", { lineHeight: "16px", fontWeight: "500" }]
      }
    }
  }
}