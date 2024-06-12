<script setup lang="ts">
import PhotoSwipeLightbox from "photoswipe/lightbox";
import "photoswipe/style.css";

const nuxtApp = useNuxtApp();

const { data: translations, refresh } = useFetch(setApiUrl("/translations/stages"), {
  headers: { "X-User-Locale": useState("userLocale") },
});

const { data: images } = await useFetch(setApiUrl("/images/stages"), {
  getCachedData(key) {
    return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  },
});

const stages = ["main", "small", "children"];
const stageElements = ref([]);
const lightboxes = ref([]);

function initLightbox(stage) {
  const lightbox = new PhotoSwipeLightbox({
    gallery: `#${stage}, #${stage}Plan`,
    children: "a",
    pswpModule: () => import("photoswipe"),
  });
  lightbox.init();
  lightboxes.value.push(lightbox);
}

onMounted(async () => {
  if (stageElements.value.length === stages.length) {
    stages.forEach((stage) => initLightbox(stage));
  }
});

onUnmounted(() => {
  lightboxes.value.forEach((lightbox) => lightbox.destroy());
});
</script>

<template lang="html">
  <div class="container mt-3">
    <div v-if="translations && images" class="row justify-content-center">
      <div v-for="stage in stages" class="col-12 col-md-9 mb-3">
        <StagesStageCard>
          <template #images>
            <div ref="stageElements" :id="stage" class="pspw-gallery mb-3">
              <Swiper
                :modules="[SwiperAutoplay, SwiperEffectCoverflow, SwiperPagination]"
                :effect="'coverflow'"
                :autoplay="{
                  delay: 3500,
                  disableOnInteraction: true,
                }"
                :pagination="{
                  enabled: true,
                  type: 'bullets',
                }"
              >
                <SwiperSlide v-for="img in images[stage]" :key="img">
                  <a
                    class="carousel-item col-12 gallery-slide"
                    :href="`/media/stages/${stage}/photos/${img[0]}`"
                    :data-pswp-width="img[1]"
                    :data-pswp-height="img[2]"
                    title=""
                  >
                    <!-- <img
                      :src="`/media/stages/${stage}/photos/${img[0]}`"
                      :alt="`${stage} stage layout`"
                      class="card-img-top img-fluid"
                      :width="img[1]"
                      :height="img[2]"
                      loading="lazy"
                    /> -->
                    <NuxtImg
                      format="webp"
                      :src="`/media/stages/${stage}/photos/${img[0]}`"
                      :alt="`${stage} stage layout`"
                      class="card-img-top img-fluid"
                      :width="img[1]"
                      :height="img[2]"
                      sizes="90vw md:50vw lg:700px xl:960px"
                      :placeholder="[18, 10]"
                      loading="lazy"
                    />
                  </a>
                  <div class="swiper-lazy-preloader"></div>
                </SwiperSlide>
              </Swiper>
            </div>
          </template>

          <template #title>
            {{ translations[`${stage}_title`] }}
          </template>

          <template #cardText>
            <p v-for="p in translations[stage].split('\n')" class="lead">{{ p }}</p>
          </template>

          <template #buttons>
            <div :id="`${stage}Plan`" class="d-flex justify-content-between pspw-gallery">
              <a
                :href="`/media/stages/${stage}/plan.jpg`"
                class="btn btn-primary"
                :data-pswp-width="images[`${stage}_plan`][1]"
                :data-pswp-height="images[`${stage}_plan`][2]"
                title=""
              >
                {{ translations.floor }}
              </a>
              <a
                :href="`/media/stages/${stage}/layout.svg`"
                class="btn btn-primary"
                data-pswp-width=""
                data-pswp-height=""
                title=""
              >
                {{ translations.seating }}
              </a>
            </div>
          </template>
        </StagesStageCard>
      </div>
    </div>
  </div>
</template>

<style lang="css" scoped></style>
