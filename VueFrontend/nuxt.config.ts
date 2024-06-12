// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  css: ["~/assets/main.css"],
  modules: [
    "nuxt-icon",
    "@vueuse/nuxt",
    "@nuxtjs/i18n",
    "nuxt-swiper",
    // "@vee-validate/nuxt",
    "@nuxtjs/seo",
    "@nuxt/image",
    "@nuxtjs/device",
  ],
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ["/bg", "/en", "/sitemap.xml", "/robots.txt"],
    },
  },
  app: {
    pageTransition: { name: "page", mode: "out-in" },
  },
  image: {
    keep: true,
  },
  ogImage: {
    enabled: false,
  },
  linkChecker: {
    enabled: false,
  },
  i18n: {
    strategy: "prefix",
    baseUrl: "https://www.dktshumen.com",
    defaultLocale: "bg",
    locales: [
      {
        code: "bg",
        iso: "bg-BG",
      },
      {
        code: "en",
        iso: "en-GB",
      },
    ],
    experimental: {
      localeDetector: "./utils/localeDetector.ts",
    },
  },
});
