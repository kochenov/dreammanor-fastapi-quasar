<template>
  <div class="row-grid">
    <q-card
      v-for="item in items"
      :key="`xs-${item.id}`"
      class="my-card"
      flat
      bordered
    >
      <div class="position-relative">
        <q-img
          :ratio="16 / 9"
          :src="item.link_img || '/img/not-image-house.jpg'"
        />
        <q-icon
          v-if="item.is_video"
          class="position-absolute"
          name="camera_outdoor"
          size="25px"
          color="orange-6"
        />
      </div>

      <q-card-section>
        <q-btn
          fab
          color="primary"
          icon="place"
          class="absolute"
          style="top: 0; right: 12px; transform: translateY(-50%)"
        />

        <div class="row no-wrap items-center">
          <div class="col text-subtitle1 ellipsis">{{ item.title }}</div>
          <div
            class="col-auto text-grey text-caption q-pt-md row no-wrap items-center"
          >
            <q-icon name="place" />
            250 ft
          </div>
        </div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="text-subtitle1 text-weight-bolder text-right">
          <q-icon
            name="currency_ruble"
            style="color: green; font-size: 1.4em"
          />
          {{ format_number(item.price) }}
        </div>
        <div class="text-caption text-grey">
          {{ item.comment }}
        </div>
      </q-card-section>

      <q-separator />

      <q-card-actions>
        <q-icon name="today" size="25px">
          <q-tooltip
            anchor="top middle"
            self="bottom middle"
            :offset="[10, 10]"
          >
            {{ date_ru(item.created_ad) }}
          </q-tooltip>
        </q-icon>

        <q-btn :href="item.link" flat color="primary"> Смотреть </q-btn>
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
import { api } from "src/boot/axios";
import { date_ru, format_number } from "src/utils/helpers";
import { onMounted, ref } from "vue";

const items = ref(null);

const getListAsd = async () => {
  let res = await api.get(`/parsing/list`);
  items.value = res.data.items;
};

onMounted(async () => {
  await getListAsd();
});
</script>

<style lang="scss" scoped>
.row-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(270px, 1fr));
  gap: 30px;
  justify-content: center;
}

.position-absolute {
  bottom: 0;
  left: 0;
  position: absolute;
}
.position-relative {
  position: relative;
}
</style>
