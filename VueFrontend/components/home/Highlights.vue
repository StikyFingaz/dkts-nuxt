<script setup lang="ts">
const { data: highlights } = useNuxtData("highlights");
const { data: highlightImages } = useNuxtData("highlightImages");
const displaySize = useState("displaySize");

onMounted(() => {
  // console.log(highlights.value);
  // console.log(highlightImages.value);
});
</script>

<template lang="html">
  <div class="container">
    <div id="highlights" class="container-fluid mt-3 mb-3">
      <Swiper
        :modules="[SwiperAutoplay]"
        slidesPerView="auto"
        :centeredSlidesBounds="true"
        :centerInsufficientSlides="true"
        :autoplay="{
          delay: 3500,
          disableOnInteraction: true,
        }"
      >
        <SwiperSlide v-for="(highlight, key) in highlights" :key="key">
          <PlayCard
            :playLink="highlight.slug"
            :isCurrent="highlight.current"
            :ticket-link="highlight.entase_data?.[0]?.id ?? null"
            class="m-2"
          >
            <template #images>
              <NuxtImg
                format="webp"
                :src="`/media/plays/${highlight.slug}/poster.jpg`"
                :alt="`${highlight.name} - Poster`"
                class="card-img-top img-fluid gallery-slide"
                :width="highlightImages.posters[highlight.slug][0]"
                :height="highlightImages.posters[highlight.slug][1]"
                sizes="310px md:40vw lg:300px"
                loading="lazy"
              />
            </template>
            <template #name>
              {{ getTranslation(highlight, "name") }}
            </template>
          </PlayCard>
        </SwiperSlide>
      </Swiper>
    </div>
  </div>
</template>

<style lang="css" scoped>
.swiper-slide {
  max-width: 310px;

  @media (min-width: 768px) {
    max-width: 40vw;
  }

  @media (min-width: 992px) {
    max-width: 300px;
  }
}
</style>
