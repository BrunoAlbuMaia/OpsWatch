function Container({ children }) {
    return (
    <main className={` container mx-auto px-4 py-6 `}>
        {children}
    </main>
    );
  }
  
  export default Container;