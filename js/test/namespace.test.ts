import { Namespace } from '../src/namespace';


describe('ftm/Namespace class', () => {
  const namespaceInstance = new Namespace('test_namespace');
  const testId = '3f4e94b5e30aa66090df8f4bf9e701e4f4061fdf';
  const testId2 = 'e701e4f4061f45345354df';
  let testSignedId: string;
  let testSignedId2: string;

  beforeAll(async () => {
    testSignedId = await namespaceInstance.sign(testId);
    testSignedId2 = await namespaceInstance.sign(testId2);
  });

  it('should be instantiable', () => {
    expect(namespaceInstance).toBeInstanceOf(Namespace)
  })

  describe('method parse', () => {
    it('should exist', () => {
      expect(namespaceInstance).toHaveProperty('parse')
    })
    it('should return a separated namespace and entity', function () {
      expect(namespaceInstance.parse(testSignedId)).toHaveLength(2);
      expect(namespaceInstance.parse(testSignedId)[0]).toStrictEqual(testId);
    })
    it('should handle non-namespaced ids', function () {
      expect(namespaceInstance.parse(testId)).toStrictEqual([testId]);
    })
  })

  describe('method sign', () => {
    it('should exist', () => {
      expect(namespaceInstance).toHaveProperty('sign')
    })
    it('should return the input if input id is empty', async function () {
      expect(await namespaceInstance.sign('')).toBe('');
    })
    it('should return the input id if no namespace given', async function () {
      const emptyNamespace = new Namespace('');
      const signed = await emptyNamespace.sign(testId);
      expect(signed).toBe(testId);
    })
    it('should return a signed entityId', async function () {
      const re = new RegExp(`${testId}\..*`)
      expect(await namespaceInstance.sign(testSignedId)).toMatch(re);
    })
    it('should be able to sign multiple ids', async function () {
      const testSignedId = await namespaceInstance.sign(testId);
      const testSignedId2 = await namespaceInstance.sign(testId2);
      const [signedId1, digest1] = testSignedId.split('.');
      const [signedId1a, digest1a] = testSignedId.split('.');
      const [signedId2, digest2] = testSignedId2.split('.');

      expect(signedId1).toMatch(testId);
      expect(digest1).toMatch(digest1a);
      expect(signedId2).toMatch(testId2);
    })
  })
})
