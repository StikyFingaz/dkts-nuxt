<script setup lang="ts">
const nuxtApp = useNuxtApp();
const userLocale = useState("userLocale");

const { data: commonStrings } = useNuxtData("commonStrings");

const { data: homeStrings, refresh: refreshHomeStrings } = await useFetch(setApiUrl("/translations/home"), {
  key: "homeStrings",
  headers: {
    "X-User-Locale": useState("userLocale"),
  },
  // getCachedData(key) {
  //   return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  // },
});

const { data: events, refresh: refreshEvents } = await useFetch(setApiUrl("/calendar/"), {
  key: "calendar",
  headers: {
    "X-User-Locale": useState("userLocale"),
    "X-User-Timezone": useState("userTimezone"),
  },
  // getCachedData(key) {
  //   return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  // },
});

const { data: highlights, refresh: refreshHighlights } = await useFetch(setApiUrl("/plays/highlights"), {
  key: "highlights",
  headers: { "X-User-Locale": useState("userLocale") },
  // getCachedData(key) {
  //   return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  // },
});

const { data: highlightImages } = await useFetch(setApiUrl("/images/highlights"), {
  key: "highlightImages",
  getCachedData(key) {
    return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  },
});

const { data: carouselImages } = await useFetch(setApiUrl("/images/main-carousel"), {
  key: "carouselImages",
  getCachedData(key) {
    return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  },
});

const { data: sponsorLogos } = await useFetch(setApiUrl("/images/sponsors"), {
  key: "sponsorLogos",
  getCachedData(key) {
    return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  },
});

onMounted(async () => {
  await refreshEvents;
  // try {
  //   await Promise.all([refreshEvents()]);
  // } catch (error) {
  //   console.error("Error fetching data:", error);
  // }
});
</script>

<template lang="html">
  <div id="homeContainer">
    <div id="mainCarousel">
      <!-- <HomeMobileCarousel /> -->
      <HomeDesktopCarousel />
    </div>
    <div id="eventsTable" class="container">
      <HomeEventsTable />
    </div>
    <div
      id="currentHighlights"
      class="container-fluid d-flex text-bg-dark justify-content-center mt-4 mb-3"
      data-bs-theme="light"
    >
      <HomeHighlights />
    </div>
    <div id="mainAccent" class="container" data-bs-theme="light">
      <HomeMainAccent :mainAccent="highlights[0]" />
    </div>
    <HomeSponsors />
  </div>
</template>

<style lang="css" scoped>
@media (max-width: 576px) {
  #mainCarousel {
    min-height: 55vh;
  }
}

@media (min-width: 1024px) {
  #mainCarousel {
    min-height: 55vh;
  }
}
</style>
