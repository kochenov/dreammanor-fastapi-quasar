/**
 *  declOfNum(1, ['минута', 'минуты', 'минут']); // вернёт — минута
 *  declOfNum(2, ['минута', 'минуты', 'минут']); // вернёт — минуты
 *  declOfNum(5, ['минута', 'минуты', 'минут']); // вернёт — минут
 * @param {*} number
 * @param {*} words
 * @returns
 */
export const wordNum = (number, words) => {
  return words[
    number % 100 > 4 && number % 100 < 20
      ? 2
      : [2, 0, 1, 1, 1, 2][number % 10 < 5 ? Math.abs(number) % 10 : 5]
  ];
};

import {date} from "quasar"
/**
 * Возвращает отформатированную дату
 * @param {*} my_date Дата в полном формате
 * @returns отформатированную дату
 */
export const date_ru = (my_date) => {

  return date.formatDate(my_date, 'DD.MM.YYYY')
};
/**
 * вернёт отформатированное число
 * @param {*} num
 * @returns
 */
export const format_number = (num) => {

  return num.toLocaleString();
};
