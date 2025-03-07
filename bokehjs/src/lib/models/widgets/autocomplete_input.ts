import {TextInput, TextInputView} from "./text_input"

import {empty, display, undisplay, div, Keys} from "core/dom"
import * as p from "core/properties"
import {clamp} from "core/util/math"

import {bk_below, bk_active} from "styles/mixins"
import {bk_menu} from "styles/menus"

export class AutocompleteInputView extends TextInputView {
  model: AutocompleteInput

  protected _open: boolean = false

  protected _last_value: string = ""

  protected _hover_index: number = 0

  protected menu: HTMLElement

  render(): void {
    super.render()

    this.input_el.addEventListener("keydown", (event) => this._keydown(event))
    this.input_el.addEventListener("keyup", (event) => this._keyup(event))

    this.menu = div({class: [bk_menu, bk_below]})
    this.menu.addEventListener("click", (event) => this._menu_click(event))
    this.menu.addEventListener("mouseover", (event) => this._menu_hover(event))
    this.el.appendChild(this.menu)
    undisplay(this.menu)
  }

  change_input(): void {
    if (this._open && this.menu.children.length > 0) {
      this.model.value = this.menu.children[this._hover_index].textContent!
      this.input_el.focus()
      this._hide_menu()
    }
  }

  protected _update_completions(completions: string[]): void {
    empty(this.menu)

    for (const text of completions) {
      const item = div({}, text)
      this.menu.appendChild(item)
    }
    if (completions.length > 0)
      this.menu.children[0].classList.add(bk_active)

  }

  protected _show_menu(): void {
    if (!this._open) {
      this._open = true
      this._hover_index = 0
      this._last_value = this.model.value
      display(this.menu)

      const listener = (event: MouseEvent) => {
        const {target} = event
        if (target instanceof HTMLElement && !this.el.contains(target)) {
          document.removeEventListener("click", listener)
          this._hide_menu()
        }
      }
      document.addEventListener("click", listener)
    }
  }

  protected _hide_menu(): void {
    if (this._open) {
      this._open = false
      undisplay(this.menu)
    }
  }

  protected _menu_click(event: MouseEvent): void {
    if (event.target != event.currentTarget && event.target instanceof Element) {
      this.model.value = event.target.textContent!
      this.input_el.focus()
      this._hide_menu()
    }
  }

  protected _menu_hover(event: MouseEvent): void {
    if (event.target != event.currentTarget && event.target instanceof Element) {
      let i = 0
      for (i = 0; i<this.menu.children.length; i++) {
        if (this.menu.children[i].textContent! == event.target.textContent!)
          break
      }
      this._bump_hover(i)
    }
  }

  protected _bump_hover(new_index: number): void {
    const n_children = this.menu.children.length
    if (this._open && n_children > 0) {
      this.menu.children[this._hover_index].classList.remove(bk_active)
      this._hover_index = clamp(new_index, 0, n_children-1)
      this.menu.children[this._hover_index].classList.add(bk_active)
    }
  }

  _keydown(_event: KeyboardEvent): void {}

  _keyup(event: KeyboardEvent): void {
    switch (event.keyCode) {
      case Keys.Enter: {
        this.change_input()
        break
      }
      case Keys.Esc: {
        this._hide_menu()
        break
      }
      case Keys.Up: {
        this._bump_hover(this._hover_index-1)
        break
      }
      case Keys.Down: {
        this._bump_hover(this._hover_index+1)
        break
      }
      default: {
        const value = this.input_el.value

        if (value.length < this.model.min_characters) {
          this._hide_menu()
          return
        }

        const completions: string[] = []
        for (const text of this.model.completions) {
          if (text.startsWith(value))
            completions.push(text)
        }

        this._update_completions(completions)

        if (completions.length == 0)
          this._hide_menu()
        else
          this._show_menu()
      }
    }
  }
}

export namespace AutocompleteInput {
  export type Attrs = p.AttrsOf<Props>

  export type Props = TextInput.Props & {
    completions: p.Property<string[]>
    min_characters: p.Property<number>
  }
}

export interface AutocompleteInput extends AutocompleteInput.Attrs {}

export class AutocompleteInput extends TextInput {
  properties: AutocompleteInput.Props

  constructor(attrs?: Partial<AutocompleteInput.Attrs>) {
    super(attrs)
  }

  static initClass(): void {
    this.prototype.default_view = AutocompleteInputView

    this.define<AutocompleteInput.Props>({
      completions:    [ p.Array, [] ],
      min_characters: [ p.Int,   2  ],
    })
  }
}
AutocompleteInput.initClass()
