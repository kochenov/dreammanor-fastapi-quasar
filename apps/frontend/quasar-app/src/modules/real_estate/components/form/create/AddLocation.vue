<template>
  <!-- Адрес -->
  <div class="row q-mt-sm wrap q-col-gutter-md">
    <q-select
      :key="modal_form_add_region"
      class="col-12 col-sm"
      v-model="form_data.region"
      filled
      use-input
      input-debounce="0"
      label="Выбрать регион"
      :options="region_id_options"
      @update:modelValue="loadDistrict()"
      @filter="region_id_filter_fn"
      behavior="dialog"
      :loading="load_regions_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список регионов пуст. Добавьте новый регион
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_region = true"
        />
      </template>
      <q-dialog
        v-model="modal_form_add_region"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить новый регион</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_region"
              label="Введите название региона"
              dense
              error-message="Такой регион уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_region_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      :key="modal_form_add_district"
      class="col-12 col-sm"
      v-model="form_data.district"
      filled
      :disable="!form_data.region && load_regions_status"
      :error="!form_data.region"
      error-message="Выбирите сначала регион"
      use-input
      input-debounce="0"
      label="Выбрать район"
      :options="district_id_options"
      @update:modelValue="loadSettlementTypes()"
      @filter="district_id_filter_fn"
      behavior="dialog"
      :loading="load_districts_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список районов пуст. Добавьте новый район
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_district = true"
        />
      </template>
      <q-dialog
        v-if="form_data.region"
        v-model="modal_form_add_district"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить новый район</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_district"
              label="Введите название региона"
              dense
              error-message="Такой регион уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_district_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      :key="modal_form_add_settlement_type"
      class="col-12 col-sm"
      v-model="form_data.settlement_type"
      filled
      use-input
      input-debounce="0"
      label="Выбрать тип поселения"
      :options="settlement_type_id_options"
      @update:modelValue="loadSettlements"
      @filter="settlement_type_id_filter_fn"
      behavior="dialog"
      :loading="load_settlement_types_status"
      :disable="!form_data.region || !form_data.district"
      :error="!form_data.region || !form_data.district"
      error-message="Выбирите сначала регион и район"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список типов поселений пуст. Добавьте новый тип
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_settlement_type = true"
        />
      </template>
      <q-dialog
        v-model="modal_form_add_settlement_type"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить тип поселения</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_settlement_type"
              label="Введите название типа поселения"
              dense
              error-message="Такой тип уже есть"
            />
            <q-input
              class="q-pt-md"
              v-model="new_settlement_type_i"
              label="Как будет на вопрос где?"
              dense
              error-message="Такой тип уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn
              flat
              label="ДОБАВИТЬ"
              @click="save_new_settlement_type_to_base"
            />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>

    <q-select
      @blur="updateFullAdress"
      :key="modal_form_add_settlement"
      class="col-12 col-sm"
      v-model="form_data.settlement"
      filled
      :disable="
        !form_data.region || !form_data.district || !form_data.settlement_type
      "
      :error="
        !form_data.region || !form_data.district || !form_data.settlement_type
      "
      error-message="Выбирите сначала регион, район и тип поселения"
      use-input
      input-debounce="0"
      label="Выбрать поселение"
      :options="settlement_id_options"
      @focus="loadSettlements()"
      @filter="settlement_id_filter_fn"
      behavior="dialog"
      :loading="load_settlements_status"
    >
      <template v-slot:no-option>
        <q-item>
          <q-item-section class="text-grey">
            Список поселений пуст. Добавьте новое поселение
          </q-item-section>
        </q-item>
      </template>
      <template v-slot:append>
        <q-btn
          round
          dense
          flat
          icon="add"
          @click.stop.prevent="modal_form_add_settlement = true"
        />
      </template>
      <q-dialog
        v-if="form_data.region && form_data.district"
        v-model="modal_form_add_settlement"
        persistent
        transition-show="flip-down"
        transition-hide="flip-up"
      >
        <q-card style="width: 300px">
          <q-card-section>
            <div class="text-h6">Добавить поселение</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            <q-input
              v-model="new_settlement"
              label="Введите название поселения"
              dense
              error-message="Такое поселение уже есть"
            />
            <q-input
              class="q-pt-md"
              v-model="new_settlement_i"
              label="Как будет на вопрос Где?"
              dense
              error-message="Такое поселение уже есть"
            />
          </q-card-section>

          <q-card-actions align="right" class="bg-white text-teal">
            <q-btn flat label="ОТМЕНА" color="red" v-close-popup />
            <q-btn flat label="ДОБАВИТЬ" @click="save_new_settlement_to_base" />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </q-select>
  </div>

  <q-separator color="orange q-my-lg" inset />

  <!-- Полный адрес -->
  <q-input
    class="q-my-md"
    filled
    autocomplete="Off"
    v-model="form_data.full_adress"
    label="Полный адрес *"
    hint="Полный адрес в формате: Регион, район, село, улица, № дома"
    lazy-rules
    :rules="[(val) => (val && val.length > 0) || 'Заполнять обязательно']"
  />
</template>

<script setup>
import { ref } from 'vue';


// модели формы
const full_adress = ref(); // полный адрес
const region = ref(); // регион
const district = ref(); // район
const settlement = ref(); // поселение


const form_data = ref({
  title: "",
  description: "",
  meta_title: "",
  meta_description: "",
  status: false,
  region: null,
  district: null,
  settlement_type: null,
  settlement: null,
  full_adress: null,
  main_image: null,
  video_zen: null,
  video_rutube: null,
  link_to_ads: null,
  price: null,
  area_of_house: null,
  plot_area: null,
  bathroom_in_house: false,
  gaz: false,
  uid: null,
  //
  number_of_rooms: null,
  number_of_floors: null,
  sauna: false,
  plastic_windows: false,
  bus_stop: false,
  rail_station: false,
  distance_to_the_river: null,
  distance_to_the_lake: null,
  there_is_a_forest_nearby: false,
  distance_to_the_city: null,
  gas_heating: false,
  furnace_heating: false,
  sewerage: false,
  year_of_construction: null,
  wall_material_id: null,
  alarm_status: false,
});

</script>

<style lang="scss" scoped></style>
