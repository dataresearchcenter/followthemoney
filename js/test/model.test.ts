import { Entity } from '../src'
import modelData from '../src/defaultModel.json'
import { Model } from '../src/model'
import { Schema } from '../src/schema'


describe('ftm/Model class', () => {
  it('should be instantiable', () => {
    const model = { schemata: {}, types: {} }
    expect(new Model(model)).toBeInstanceOf(Model)
  })
  describe('getSchema method', () => {
    let modelInstance: Model
    beforeEach(() => {
      modelInstance = new Model(modelData)
    })

    it('should exist', () => {
      expect(modelInstance).toHaveProperty('getSchema')
    })

    it('should return `Schema` instance for associated name', () => {
      const schema = modelInstance.getSchema('Thing')
      expect(schema).toBeInstanceOf(Schema)
      const other = modelInstance.getSchema(schema);
      expect(other).toBe(schema)
    })

    it('should fail for unknown schema', () => {
      expect(() => {
        modelInstance.getSchema('Banana')
      }).toThrow(Error)
    })
  })
  describe('method createEntity', () => {
    let modelInstance: Model
    beforeEach(() => {
      modelInstance = new Model(modelData)
    })
    it('should exist', () => {
      expect(modelInstance).toHaveProperty('createEntity')
    })
    it('should return a instance of Entity', async function () {
      const entity = await modelInstance.createEntity('Person');
      expect(entity).toBeInstanceOf(Entity);
    })
  })
  describe('method getEntity', () => {
    let modelInstance: Model
    beforeEach(() => {
      modelInstance = new Model(modelData)
    })
    it('should exist', () => {
      expect(modelInstance).toHaveProperty('getEntity')
    })
    it('should return a instance of Entity', function () {
      const data = {
        id: 'banana',
        schema: 'Person',
        properties: {
          name: ['Mr. Banana']
        }
      }
      expect(modelInstance.getEntity(data))
        .toBeInstanceOf(Entity);
    })
  })
  it('should contain `schemata` metadata', () => {
    const model = new Model(modelData)
    expect(model).toHaveProperty('schemata')
  });

})
