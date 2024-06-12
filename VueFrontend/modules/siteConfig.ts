import { defineNuxtModule } from "nuxt/kit";
import { installNuxtSiteConfig, updateSiteConfig } from "nuxt-site-config-kit";

export default defineNuxtModule({
  // ...
  async setup(options) {
    await installNuxtSiteConfig();

    // Optional: set some site config from your modules options
    // This is not recommended, only to keep supporting your modules options
    updateSiteConfig({
      _context: "my-module",
      url: options.siteUrl,
    });
  },
});
