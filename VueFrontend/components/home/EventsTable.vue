<script setup lang="ts">
const userLocale = useState("userLocale");

const { data: translations } = useNuxtData("homeStrings");
const { data: events } = useNuxtData("calendar");

onMounted(async () => {
  // if (error.value) {
  //   console.error("Failed to fetch play data:", error.value);
  // }
});
</script>

<template lang="html">
  <div id="tableContainer" class="container col-lg-10 col-xl-9 mt-2 mt-md-3">
    <div id="eventsTable" class="table-responsive custom-scrollbar" data-bs-theme="light">
      <table class="table table-hover table-sm">
        <thead id="tableHeader">
          <tr>
            <th class="fs-5" colSpan="4">{{ translations.upcoming }}</th>
            <!-- <th class="d-none d-md-table-cell"></th> -->
            <!-- <th></th> -->
            <!-- <th></th> -->
          </tr>
          <tr class="table-group-divider"></tr>
        </thead>
        <tbody>
          <template v-for="(dailyEvents, date) in events" :key="date">
            <tr>
              <th scope="row" :rowspan="dailyEvents.length + 1">
                <div class="row align-items-center">
                  <div id="dayNum" class="col-md-5 text-start text-md-end fs-1 ps-2 pe-1">
                    {{ date.split("-")[0] }}.
                  </div>
                  <div id="dayMonth" class="col-md-7 ps-2 pe-3">
                    <span>{{ date.split("-")[1] }}</span>
                    <br />
                    <span class="text-muted">{{ date.split("-")[2] }}</span>
                  </div>
                </div>
              </th>
            </tr>
            <template v-for="event in dailyEvents">
              <tr class="align-middle">
                <td class="d-none d-md-table-cell ps-3 fs-5">{{ event.eventStart }}</td>
                <td>
                  <span class="d-table-cell d-md-none fs-5">{{ event.eventStart }}</span>
                  <NuxtLinkLocale :to="`/events/plays/${event.eventDetails.slug}`" id="playLink">
                    <span class="link-dark fw-bold fs-5">
                      {{ getTranslation(event.eventDetails, "name") }}
                    </span>
                  </NuxtLinkLocale>
                </td>
                <td>
                  <a
                    v-if="event.eventID"
                    tabindex="0"
                    id="ticketButton"
                    class="btn btn-outline-primary border border-0 d-flex align-items-center ps-2 pe-2"
                    role="button"
                    :href="`https://www.entase.bg/book?eid=${event.eventID}&lc=${userLocale}`"
                    @click.prevent="openTicketPopup(`https://www.entase.bg/book?eid=${event.eventID}&lc=${userLocale}`)"
                  >
                    <Icon class="me-1" name="bi:ticket-perforated" />
                    {{ translations.ticket }}
                  </a>
                </td>
              </tr>
            </template>
            <tr class="table-group-divider"></tr>
          </template>
        </tbody>
      </table>
    </div>
  </div>
</template>

<style lang="css" scoped>
.custom-scrollbar::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: #f5f5f5;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 12px;
  background-color: #f5f5f5;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  border-radius: 10px;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  background-color: #555;
}

#dayMonth {
  text-transform: capitalize;
}

@media (max-width: 576px) {
  #eventsTable {
    min-height: 45vh;
  }
}

#eventsTable {
  max-height: 30vh;
}

#tableHeader {
  position: sticky;
  top: 0;
}

#playLink {
  text-decoration: none;
}

#ticketButton {
  max-width: min-content;
}
</style>
