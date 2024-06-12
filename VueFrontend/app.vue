<script setup lang="ts">
const nuxtApp = useNuxtApp();

const userLocale = useState("userLocale", () => nuxtApp.$i18n.locale.value);
const userTimezone = useState("userTimezone", () => Intl.DateTimeFormat().resolvedOptions().timeZone);

const { data: commonStrings } = await useFetch(setApiUrl("/translations"), {
  key: "commonStrings",
  headers: { "X-User-Locale": useState("userLocale") },
});

const { data: actorData } = await useFetch(setApiUrl("/search/actors"), {
  headers: { "X-User-Locale": useState("userLocale") },
});

const { data: playData } = await useFetch(setApiUrl("/search/plays"), {
  headers: { "X-User-Locale": useState("userLocale") },
});

const searchData = useState("searchData", () => actorData.value.concat(playData.value));
const { width } = useWindowSize();
const displaySize = useState("displaySize", () => "");

watchEffect(() => {
  userLocale.value = nuxtApp.$i18n.locale.value;
  searchData.value = actorData.value.concat(playData.value);
  displaySize.value = getDisplaySize(width.value);
});

useSeoMeta({
  title: () => commonStrings.value.title,
  description: () => commonStrings.value.description,
  ogTitle: () => commonStrings.value.title,
  ogDescription: () => commonStrings.value.description,
  ogImage: "/index.jpg",
  ogUrl: "https://www.dktshumen.com",
  twitterTitle: () => commonStrings.value.title,
  twitterDescription: () => commonStrings.value.description,
  twitterImage: "/index.jpg",
  twitterCard: "summary",
});

onMounted(() => {
  // if (tError.value) {
  //   console.error("Failed to fetch play data:", tError.value);
  // }
});
</script>

<template>
  <NuxtLayout name="default">
    <NuxtLoadingIndicator />
    <NuxtPage />
  </NuxtLayout>
</template>

<style lang="css">
.page-enter-active,
.page-leave-active {
  transition: all 0.4s;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(1rem);
}
</style>
