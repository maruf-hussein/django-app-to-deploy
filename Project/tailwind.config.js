/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "templates/**/*.html", // Add paths to other apps if necessary
  ],
  darkMode: "class",
  theme: {
    extend: {
      backgroundImage: theme => ({
        'logo-dark': `url('../images/logo_dark.png')`,
        'logo-light': `url('../images/logo_light.png')`,
      }),
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        "neutral-150": "#f0f0f0"
      },
    },
  },
  plugins: [],
};
