import {PointGeometry} from 'core/geometry'
import {Arrayable} from "core/types"
import {Area, AreaView, AreaData} from "./area"
import {Context2d} from "core/util/canvas"
import {SpatialIndex, IndexedRect} from "core/util/spatial"
import * as hittest from "core/hittest"
import * as p from "core/properties"
import {Selection} from "../selections/selection"

export interface VAreaData extends AreaData {
  _x: Arrayable<number>
  _y1: Arrayable<number>
  _y2: Arrayable<number>

  sx: Arrayable<number>
  sy1: Arrayable<number>
  sy2: Arrayable<number>
}

export interface VAreaView extends VAreaData {}

export class VAreaView extends AreaView {
  model: VArea
  visuals: VArea.Visuals

  protected _index_data(): SpatialIndex {
    const points: IndexedRect[] = []

    for (let i = 0, end = this._x.length; i < end; i++) {
      const x = this._x[i]
      const y1 = this._y1[i]
      const y2 = this._y2[i]

      if (isNaN(x + y1 + y2) || !isFinite(x + y1 + y2))
        continue

      points.push({x0: x, y0: Math.min(y1, y2), x1: x, y1: Math.max(y1, y2), i})
    }

    return new SpatialIndex(points)
  }

  protected _inner(ctx: Context2d, sx: Arrayable<number>, sy1: Arrayable<number>, sy2: Arrayable<number>, func: (this: Context2d) => void): void {
    ctx.beginPath()
    for (let i = 0, end = sy1.length; i < end; i++) {
      ctx.lineTo(sx[i], sy1[i])
    }
    // iterate backwards so that the upper end is below the lower start
    for (let start = sy2.length-1, i = start; i >= 0; i--) {
      ctx.lineTo(sx[i], sy2[i])
    }
    ctx.closePath()
    func.call(ctx)
  }

  protected _render(ctx: Context2d, _indices: number[], {sx, sy1, sy2}: VAreaData): void {

    if (this.visuals.fill.doit) {
      this.visuals.fill.set_value(ctx)
      this._inner(ctx, sx, sy1, sy2, ctx.fill)
    }

    this.visuals.hatch.doit2(ctx, 0, () => this._inner(ctx, sx, sy1, sy2, ctx.fill), () => this.renderer.request_render())

  }

  scenterx(i: number): number {
    return this.sx[i]
  }

  scentery(i: number): number {
    return (this.sy1[i] + this.sy2[i])/2
  }

  protected _hit_point(geometry: PointGeometry): Selection {
    const result = hittest.create_empty_hit_test_result()

    const L = this.sx.length
    const sx = new Float64Array(2*L)
    const sy = new Float64Array(2*L)

    for (let i = 0, end = L; i < end; i++) {
      sx[i] = this.sx[i]
      sy[i] = this.sy1[i]
      sx[L+i] = this.sx[L-i-1]
      sy[L+i] = this.sy2[L-i-1]
    }

    if (hittest.point_in_poly(geometry.sx, geometry.sy, sx, sy)) {
      result.add_to_selected_glyphs(this.model)
      result.get_view = () => this
    }

    return result
  }

  protected _map_data(): void {
    this.sx  = this.renderer.xscale.v_compute(this._x)
    this.sy1 = this.renderer.yscale.v_compute(this._y1)
    this.sy2 = this.renderer.yscale.v_compute(this._y2)
  }
}

export namespace VArea {
  export type Attrs = p.AttrsOf<Props>

  export type Props = Area.Props & {
    x: p.CoordinateSpec
    y1: p.CoordinateSpec
    y2: p.CoordinateSpec
  }

  export type Visuals = Area.Visuals
}

export interface VArea extends VArea.Attrs {}

export class VArea extends Area {
  properties: VArea.Props

  constructor(attrs?: Partial<VArea.Attrs>) {
    super(attrs)
  }

  static initClass(): void {
    this.prototype.default_view = VAreaView

    this.define<VArea.Props>({
      x:  [ p.CoordinateSpec ],
      y1: [ p.CoordinateSpec ],
      y2: [ p.CoordinateSpec ],
    })
  }
}
VArea.initClass()
