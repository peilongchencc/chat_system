LangChain中FAISS类的部分代码如下，我想要继承这个类并重写其中的`similarity_search`方法，让`similarity_search`也返回分数，应该怎么做？

```python
class FAISS(VectorStore):
    """`Meta Faiss` vector store.

    To use, you must have the ``faiss`` python package installed.

    Example:
        .. code-block:: python

            from langchain_community.embeddings.openai import OpenAIEmbeddings
            from langchain_community.vectorstores import FAISS

            embeddings = OpenAIEmbeddings()
            texts = ["FAISS is an important library", "LangChain supports FAISS"]
            faiss = FAISS.from_texts(texts, embeddings)

    """

    def __init__(
        self,
        embedding_function: Union[
            Callable[[str], List[float]],
            Embeddings,
        ],
        index: Any,
        docstore: Docstore,
        index_to_docstore_id: Dict[int, str],
        relevance_score_fn: Optional[Callable[[float], float]] = None,
        normalize_L2: bool = False,
        distance_strategy: DistanceStrategy = DistanceStrategy.EUCLIDEAN_DISTANCE,
    ):
        """Initialize with necessary components."""
        if not isinstance(embedding_function, Embeddings):
            logger.warning(
                "`embedding_function` is expected to be an Embeddings object, support "
                "for passing in a function will soon be removed."
            )
        self.embedding_function = embedding_function
        self.index = index
        self.docstore = docstore
        self.index_to_docstore_id = index_to_docstore_id
        self.distance_strategy = distance_strategy
        self.override_relevance_score_fn = relevance_score_fn
        self._normalize_L2 = normalize_L2
        if (
            self.distance_strategy != DistanceStrategy.EUCLIDEAN_DISTANCE
            and self._normalize_L2
        ):
            warnings.warn(
                "Normalizing L2 is not applicable for metric type: {strategy}".format(
                    strategy=self.distance_strategy
                )
            )

    # 其他代码省略

    def similarity_search(
        self,
        query: str,
        k: int = 4,
        filter: Optional[Union[Callable, Dict[str, Any]]] = None,
        fetch_k: int = 20,
        **kwargs: Any,
    ) -> List[Document]:
        """Return docs most similar to query.

        Args:
            query: Text to look up documents similar to.
            k: Number of Documents to return. Defaults to 4.
            filter: (Optional[Dict[str, str]]): Filter by metadata. Defaults to None.
            fetch_k: (Optional[int]) Number of Documents to fetch before filtering.
                      Defaults to 20.

        Returns:
            List of Documents most similar to the query.
        """
        docs_and_scores = self.similarity_search_with_score(
            query, k, filter=filter, fetch_k=fetch_k, **kwargs
        )
        return [doc for doc, _ in docs_and_scores]
```