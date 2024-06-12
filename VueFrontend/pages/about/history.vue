<script setup lang="ts">
const nuxtApp = useNuxtApp();

const { data: translations, refresh } = await useFetch(setApiUrl("/translations/history"), {
  headers: { "X-User-Locale": useState("userLocale") },
});

const { data: images } = await useFetch(setApiUrl("/images/history"), {
  getCachedData(key) {
    return nuxtApp.payload.data[key] || nuxtApp.static.data[key];
  },
});

onMounted(async () => {
  // await refresh();
});
</script>

<template lang="html">
  <div class="container mt-3">
    <div class="row justify-content-center">
      <div class="col-12 col-lg-11 text-center">
        <img
          format="webp"
          :src="`/media/history/${images['top'][0]}`"
          alt=""
          class="img-fluid"
          :width="images['top'][1]"
          :height="images['top'][2]"
          sizes=""
        />
      </div>
      <div class="text-center">
        <h1 class="display-4">{{ translations["text_title"] }}</h1>
      </div>
    </div>
    <!-- P 1 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p1 }}
      </template>
    </HistoryParagraph>
    <!-- P 2 -->
    <HistoryParagraph>
      <template #images>
        <figure class="figure col-12 col-md-4 col-xl-2 float-end">
          <img
            format="webp"
            :src="`/media/history/${images['1'][0]}`"
            alt=""
            class="img-fluid w-100"
            :width="images[1][1]"
            :height="images[1][2]"
            sizes=""
            placeholder
            loading="lazy"
          />
          <figcaption class="figure-caption text-center">{{ translations["pic1"] }}</figcaption>
        </figure>
      </template>
      <template #text>
        {{ translations.p2 }}
      </template>
    </HistoryParagraph>
    <!-- P 3 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p3 }}
      </template>
    </HistoryParagraph>
    <!-- P 4 -->
    <HistoryParagraph>
      <template #images>
        <div class="row justify-content-center">
          <figure class="figure col-12 col-md-11 col-lg-9">
            <img
              format="webp"
              :src="`/media/history/${images['2'][0]}`"
              alt=""
              class="img-fluid w-100"
              :width="images[2][1]"
              :height="images[2][2]"
              sizes=""
              placeholder
              loading="lazy"
            />
            <figcaption class="figure-caption text-center">{{ translations["pic2"] }}</figcaption>
          </figure>
        </div>
      </template>
      <template #text>
        {{ translations.p4 }}
      </template>
    </HistoryParagraph>
    <!-- P 5 -->
    <HistoryParagraph>
      <template #images>
        <figure class="figure col-12 col-md-4 col-xl-3 float-end">
          <img
            format="webp"
            :src="`/media/history/${images['3'][0]}`"
            alt=""
            class="img-fluid w-100"
            :width="images[3][1]"
            :height="images[3][2]"
            sizes=""
            placeholder
            loading="lazy"
          />
          <figcaption class="figure-caption text-center">{{ translations["pic3"] }}</figcaption>
        </figure>
      </template>
      <template #text>
        {{ translations.p5 }}
      </template>
    </HistoryParagraph>
    <!-- P 6 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p6 }}
      </template>
    </HistoryParagraph>
    <div class="row align-items-center">
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['4'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[4][1]"
          :height="images[4][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic4"] }}</figcaption>
      </figure>
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['5'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[5][1]"
          :height="images[5][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic5"] }}</figcaption>
      </figure>
    </div>
    <!-- P 7 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p7 }}
        <br />
        <br />
        {{ translations.p8 }}
        <br />
        <br />
        {{ translations.p9 }}
        <br />
        <br />
        {{ translations.p10 }}
        <br />
        <br />
        {{ translations.p11 }}
      </template>
    </HistoryParagraph>
    <div class="row align-items-center">
      <figure class="figure col-12 col-md-5">
        <img
          format="webp"
          :src="`/media/history/${images['6'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[6][1]"
          :height="images[6][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic6"] }}</figcaption>
      </figure>
      <figure class="figure col-12 col-md-3">
        <img
          format="webp"
          :src="`/media/history/${images['7'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[7][1]"
          :height="images[7][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic7"] }}</figcaption>
      </figure>
      <figure class="figure col-12 col-md-4">
        <img
          format="webp"
          :src="`/media/history/${images['8'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[8][1]"
          :height="images[8][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic8"] }}</figcaption>
      </figure>
    </div>
    <!-- P 8 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p12 }}
        <br />
        <br />
        {{ translations.p13 }}
        <br />
        <br />
        {{ translations.p14 }}
        <br />
        <br />
        {{ translations.p15 }}
      </template>
    </HistoryParagraph>
    <!-- P 9 -->
    <HistoryParagraph>
      <template #images>
        <figure class="figure col-12 col-md-4 col-xl-3 float-end">
          <img
            format="webp"
            :src="`/media/history/${images['9'][0]}`"
            alt=""
            class="img-fluid w-100"
            :width="images[9][1]"
            :height="images[9][2]"
            sizes=""
            placeholder
            loading="lazy"
          />
          <figcaption class="figure-caption text-center">{{ translations["pic9"] }}</figcaption>
        </figure>
      </template>
      <template #text>
        {{ translations.p16 }}
      </template>
    </HistoryParagraph>
    <!-- P 10 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p17 }}
      </template>
    </HistoryParagraph>
    <!-- P 11 -->
    <HistoryParagraph>
      <template #images>
        <figure class="figure col-12 col-md-7 col-xl-5 float-start">
          <img
            format="webp"
            :src="`/media/history/${images['10'][0]}`"
            alt=""
            class="img-fluid w-100"
            :width="images[10][1]"
            :height="images[10][2]"
            sizes=""
            placeholder
            loading="lazy"
          />
          <figcaption class="figure-caption text-center">{{ translations["pic10"] }}</figcaption>
        </figure>
      </template>
      <template #text>
        {{ translations.p18 }}
      </template>
    </HistoryParagraph>
    <!-- P 12 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p19 }}
        <br />
        <br />
        {{ translations.p20 }}
      </template>
    </HistoryParagraph>
    <div class="row align-items-center">
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['11'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[11][1]"
          :height="images[11][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic11"] }}</figcaption>
      </figure>
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['12'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[12][1]"
          :height="images[12][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic11"] }}</figcaption>
      </figure>
    </div>
    <!-- P 13 -->
    <HistoryParagraph>
      <template #text>
        {{ translations.p21 }}
        <br />
        <br />
        {{ translations.p22 }}
        <br />
        <br />
        {{ translations.p23 }}
        <br />
        <br />
        {{ translations.p24 }}
      </template>
    </HistoryParagraph>
    <div class="row">
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['13'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[13][1]"
          :height="images[13][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic12"] }}</figcaption>
      </figure>
      <figure class="figure col-12 col-md-6">
        <img
          format="webp"
          :src="`/media/history/${images['14'][0]}`"
          alt=""
          class="img-fluid w-100"
          :width="images[14][1]"
          :height="images[14][2]"
          sizes=""
          placeholder
          loading="lazy"
        />
        <figcaption class="figure-caption text-center">{{ translations["pic12"] }}</figcaption>
      </figure>
    </div>
  </div>
</template>

<style lang="css" scoped>
img {
  padding-left: 10px;
  padding-right: 10px;
}
</style>
