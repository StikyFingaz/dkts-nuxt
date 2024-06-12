<script setup lang="ts">
import Shuffle from "shufflejs";

const { data: plays } = useNuxtData("playsData");

const displaySize = useState("displaySize");
const playCards = ref(null);
const shuffleInstance = ref(null);

const isCurrent = useState("isCurrent");
const selectedAudience = useState("selectedAudience");
const selectedGenres = useState("selectedGenres");

watchEffect(() => {
  if (shuffleInstance.value) {
    shuffleInstance.value.filter((element) => useFilters(element, isCurrent, selectedAudience, selectedGenres));
  }
});

onMounted(async () => {
  shuffleInstance.value = await new Shuffle(playCards.value, {
    delimiter: ",",
    isCentered: true,
    itemSelector: ".card-col",
    group: "true",
    speed: 350,
  });
});

onUnmounted(() => {
  shuffleInstance.value.destroy();
});
</script>

<template lang="html">
  <div ref="playCards" class="row mt-3">
    <div v-for="play in plays" :data-groups="play.filter" class="col-11 col-md-6 col-lg-4 col-xl-3 mb-3 card-col">
      <PlayCard :playLink="play.slug" :isCurrent="play.current" :ticket-link="play.entase_data?.[0]?.id ?? null">
        <template #images>
          <!-- <img
            v-if="['xs', 'sm', 'md'].includes(displaySize)"
            :src="setThumborUrl(`/media/plays/${play.slug}/poster.jpg`, 'unsafe/340x0/filters:format(webp)')"
            :alt="`${play.name} - Poster`"
            class="card-img-top img-fluid d-block d-lg-none pic-sm"
            width="340"
            height="476"
            loading="lazy"
          />
          <img
            v-if="['lg', 'xl', 'xxl'].includes(displaySize)"
            :src="setThumborUrl(`/media/plays/${play.slug}/poster.jpg`, 'unsafe/310x0/filters:format(webp)')"
            :alt="`${play.name} - Poster`"
            class="card-img-top img-fluid d-none d-lg-block pic-lg"
            width="310"
            height="434"
            loading="lazy"
          /> -->
          <NuxtImg
            format="webp"
            :src="`/media/plays/${play.slug}/poster.jpg`"
            :alt="`${play.name} - Poster`"
            class="card-img-top img-fluid"
            :width="10"
            :height="14"
            sizes="90vw md:340px lg:310px"
            :placeholder="[10, 14]"
            loading="lazy"
          />
        </template>

        <template #name>
          {{ getTranslation(play, "name") }}
        </template>
      </PlayCard>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
