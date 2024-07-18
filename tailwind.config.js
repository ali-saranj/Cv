/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./**/*.{html,js}'],
  theme: {
    extend: {
      fontFamily: {
        "Rokh-Light": "Rokh Light",
        "Rokh-Med": "Rokh Medium",
        "Rokh-Bold":"Rokh Bold",
        "IRSans-Light": "IRSans Light",
        "IRSans-Medium": "IRSans Medium",
        "IRSans-Bold": "IRSans Bold"
      },
      colors:{
        "BlueC":{
          800: "#04A5E5",
          300: "#C8EBF8",
          100: "#CAF1FF"
        },
        "greenPrice":{
          800: "#1E8F0B"
        },
        "grayPro":{800:"#747474"}
      },
      container:{
        center:"true",
        padding:{
          DEFAULT:"2rem",
          lg:"4rem"
        }
      },
    },
  },
  plugins: [],
}

